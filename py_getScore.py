from cgitb import html
import time
from turtle import ht
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas
from sqlalchemy import create_engine,text
# root 后面为密码  最后为数据库
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/college_score')  # 数据库连接语句
#  TODO 下面为数据库创建和删除语句
#   创建表的时候有一个选测等级这个字段 ，其实不要这一列也没关系 ，
#   但是有个别学校在江苏招生的时候有个要求就是选测等级，没有程序会报数据库的错误。
# sql = '''DROP TABLE IF EXISTS `schools_score`'''

# with engine.connect() as connection:
#     connection.execute(text(sql))
#     connection.commit()
# sql = '''CREATE TABLE `schools_score`  (
#   `年份` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
#   `录取批次` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
#   `招生类型` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
#   `最低分/最低位次` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
#   `省控线` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
#   `专业组` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
#   `选科要求` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
#   `学校` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
#   `地区` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
#   `选测等级` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL
# );'''
# with engine.connect() as connection:
#     connection.execute(text(sql))
#     connection.commit()

def school(urls, time1):
    # # # # # # # # # # #
    chrome_option = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_option.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_option)
    # TODO 上面四行设置进入浏览器不加载图片
    #  极大提高运行速度 也可以注释掉用下面的一行  （会出现问题不建议使用）
    # driver = webdriver.Chrome()
    driver.get(urls)
    # 等待浏览器加载完成 最多等待30秒
    driver.implicitly_wait(30)
    # 可能传递的url不存在
    if driver.current_url == "https://www.gaokao.cn/":
        print(url + "不存在 （无法进入）\n")
        # 关闭浏览器
        driver.quit()
        return
    # 获取学校名
    html_school = driver.find_element(By.XPATH,
                                      '//*[@id="root"]/div/div[1]/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div[1]/div[1]/div/div[1]/div[1]').get_attribute('innerHTML')
    # 点击 出现所有省会选择
    driver.find_element(By.XPATH, '//*[@id="proline"]/div[1]/div/div[1]/div[1]/div/div').click()
    # 通过上行的点击才会产生这个html的元素  获取ul 得到里面li
    ul = driver.find_element(By.XPATH, '//*[@id="proline"]/div/div[1]/div/div[1]/div[2]/div/div/div')
    # 获取学校有多少个省份分数线 TODO 这里获取一般不会出问题很少，因为浏览器没反应过来导致获取地区为1
    lis = ul.find_elements(By.XPATH, 'div')
    length = len(lis)
    # 省级  会全部遍历
    for j in range(1, length + 1):
        # 前面已经点击了所有第一次不需要点击
        if j != 1:
            driver.find_element(By.XPATH, '//*[@id="proline"]/div[1]/div/div[1]/div[1]/div/div').click()  # 点击 出现所有省会选择
        # 需要慢一点  程序和网页速度不匹配会出错
        time.sleep(time1)
        # 点击列表里面每一个
        driver.find_element(By.XPATH, '//*[@id="proline"]/div/div[1]/div/div[1]/div[2]/div/div/div/div[' + str(j) + ']').click()
        # 获取省会
        html_province = driver.find_element(By.XPATH, '//*[@id="proline"]/div/div[1]/div/div[1]/div[1]/div/div/div').get_attribute('innerHTML')
        # 获取分数信息表格
        while True:
            # 写入html里面保存
            html_table = driver.find_element(By.XPATH, '//*[@id="proline"]/div/div[2]').get_attribute('innerHTML')
            if(html_table == "<div></div>"):
                continue
            open("table.html", 'w').write(html_table)
            break
            
        # 解析放入dfs TODO pandas库会自动解析table标签很方便
        dfs = pandas.read_html("table.html",encoding='utf-8')
        for k in dfs:
            # 表中多加两列 分别为学校和地区
            k['学校'] = html_school
            k['地区'] = html_province
            # 删除不需要的列
            if '录取率' in k.columns:
                k = k.drop(columns=['录取率'])
            # 存入csv表格 方便放入数据库
            k.to_csv("school.csv", encoding='utf-8_sig', index=False)
            # 读取本地CSV文件 准备存入数据库
            df = pandas.read_csv("school.csv", sep=',')
            # 将新建的DataFrame储存为MySQL中的数据表，不储存index列 表名为 schools_score
            df.to_sql('schools_score', engine, index=False, if_exists='append')

    print(html_school + '一共' + str(length) + "地区---数据库写入完成 正在关闭浏览器")
    print(urls + '\n')
    # 关闭浏览器
    driver.quit()

if __name__ == "__main__":
#  大学是从30开始  我也不知道多少结束 也不知道到多少本科结束到专科
#  差不多1400 中间也会有些许专科
    for i in range(40, 1050):  # 本科从30 到1050 后面也还有本科 这区域比较集中  也会参杂专科
        url = 'https://www.gaokao.cn/school/' + str(i) + '/provinceline/'
        # 传入url 和 时间  单位为秒 建议设置为0.5秒
        #   TODO  0.5秒 左右比较好 根据自己电脑配置和网速自行考虑吧 （建议0.2s以上）
        school(url, 0.3)
