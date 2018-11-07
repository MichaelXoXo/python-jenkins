"""demo.py
熟悉Python操作Jenkins
REF：
https://www.jianshu.com/p/be1d2f19c9ed
https://blog.csdn.net/seeeees/article/details/79388684
https://python-jenkins.readthedocs.io/en/latest/examples.html#example-1-get-version-of-jenkins
"""

import jenkins
from pprint import pprint
# 将“安全矩阵”替换为“登录用户可以做任何事”

# 远程Jenkins地址
jenkins_server_url = "http://100.95.135.73:8080/"

# 用户名，token值通过点击用户名查看设置获取
user_id = "jenkins"
api_token = "xxxxx"

# 登录密码
# passwd="jenkins"
# server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=passwd)

# 使用  API_Token    进行Jenkins登录操作
server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)

# 使用get.version()方法获取版本号
version = server.get_version()
user = server.get_whoami()
pprint('Hello {} form Jenkins {}'.format(user['fullName'], version))

# 打印jobs的个数
jobs_num = server.jobs_count()
pprint('Jobs count:{}'.format(jobs_num))

# 获取所有Jobs
jobs = server.get_all_jobs()
for job in jobs:
    print(job)
    print(job['name'])

# 创建job，job名字不能重复
# server.create_job('empty', jenkins.EMPTY_CONFIG_XML)

# 获取对应job的配置信息
pprint("Get job config :")
pprint(server.get_job_config("TEST"))

# 发起job，带参数，如果job没有参数，故意传参，会报错
server.build_job('TEST', {'name': 'michael'})

# 获取对应job的build相关信息
last_build_info = server.get_job_info("TEST")
pprint("Get job info :")
pprint(last_build_info)
last_success_build_number = last_build_info['lastSuccessfulBuild']['number']
laste_build_number = last_build_info['lastBuild']['number']
# laste_unsuccess_build_number = last_build_info['lastUnsuccessfulBuild']['number']
last_unstable_build = last_build_info['lastStableBuild']
builds = last_build_info['builds']  # 获取job所有的build历史记录
print(last_success_build_number)
print(laste_build_number)

# 获取job指定build number的build信息
build_info = server.get_build_info('TEST', 8)
pprint(build_info)  # build持续时间毫秒
build_parameters = build_info['actions'][0]['parameters']  # build的参数
print('Build Parameters: ')
pprint(build_parameters)

# 删除job
# server.delete_job('empty')
