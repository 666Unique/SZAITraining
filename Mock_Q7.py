# 在人机交互中，槽位是指系统需要向用户收集的关键信息。
# 以下是餐厅预订槽位设计表格。其中必填槽位是提醒时间，
# 如果用户没有表达清楚，系统会追问澄清。
# 此外，提醒内容是非必填槽位，
# 对于非必填槽位来说用户表达了系统会识别，但如果没有表达系统并不会追问。
# 现需要制定餐厅预订任务的对话设计，请观察下列“表5-1 餐厅预订槽位设计表”，
# 完成填写餐厅预订槽位设计，并在答案区完成餐厅预订槽位设计表格的填写。

# 表5-1 餐厅预订槽位设计表
# 槽位描述	类型	字段名	举例	槽位类型
# 提醒时间  必填    remind_time	明天晚上7点	时间日期
# 重复周期	非必填	cycle	每周六	重复时间
# 内容	  非必填	title	海底捞	Null
# 提醒方式 非必填 remind_type 电话提醒 提醒方式列表

#已有SimpleKernel类
alice = SimpleKernel()
alice.learn(aim_content) # learn
alice.set_variable('Age','25') #设置变量年龄

# 模拟用户输入
user_inputs = [
    '你多大',
    '你这个价格多少'
]

# 处理每个用户输入并打印响应
for user_input in user_inputs:
    print(f'Please ask: {user_input}')
    response = alice.responed(user_input)
    print(response)

# 新增匹配用户文本于AIML配置文
'''
<aiml version='1.0.1' encoding='UTF-8'>
    <category>
        <pattern>*价格*</pattern>
        <template>价格880</template>
    </category>
</aiml>
'''