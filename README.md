### 项目结构

##### data
- config.json：存放的接口测试数据，如URL地址，请求Body数据等（填写格式见后文）

##### src
- common：存放通用函数、类、模块等，方便接口用例调用执行实现自定义效果
- mainProgram：项目启动函数，项目调试debug运行函数
- testProject：测试用例存放路径，以项目为维度建立子文件夹（创建格式见后文）

##### output
- logs：存放项目运行时生成的log实时文件，具体日志内容根据自定义的log.py文件实现；
- report：存放项目运行完成时，生成的结果输出报表

##### drivers
- 本来这个文件夹是UI自动化项目中存放浏览器对应版本的驱动的，可能某些接口项目需要涉及到调用浏览器，顾浏览器驱动均放在这个目录
- 不同浏览器的浏览器驱动可以尝试建立不同文件夹即可，版本号同理


### 项目结构变更说明：

##### cookie校验机制变动
- 由每次用例函数跑之前去读取cookie方式变更为每个项目class启动后建立一次登录session方式，这样会减少验证重复工作量，提高机器性能以及测试速度

##### 数据文件变动
- 由环境划分的三套ini数据文件变更为以项目划分的一个json数据文件，减少数据重复性，以便框架结构定型，尽可能的数据分离，方便维护自动化测试用例

##### 用例继承父类变动
- 定义类的时候由继承的为unittest.TestCase变更为TemplateTeseCase，这个类中建立了类变量 env以及session  

##### 项目命名统一规范
- 每个项目单独建立在testProject文件下，包文件夹命名格式为test_xxxx
- 每个项目下分模块建立py文件，文件中建各自的功能模块类名，命名格式为XXXTest
- 每条测试用例命名为test_加上接口名称，接口名称与json文件定义的接口名称统一，命名格式为test_xxxx


### 自定义函数的改动

##### read_json.py
- 初始化函数即可根据project和env获取domain
- get_url根据fieldname和apiName获取url
- get_header带有默认参数，如果提供可以自己传入参数或者根据现有的去修改
- get_body根据前面env，project，fieldname，apiName获取都应接口请求数据
- get_robot_data根据project获取对应的钉钉入参数据

##### dingding.py
- robot_url > url参数
- mobile > 列表参数 []

##### template.py
- 继承unittest.TestCase
- 定义了环境参数变量开关
- 定义了session

##### log.py
- 改了下logs生成的地址路径

##### getTime.py
- 自定义时间戳转换的各种格式，当然你可以自定义任何格式

