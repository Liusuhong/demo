from appium import webdriver

# 在andriod 7.1.2 上面打开柠檬班app
desired_caps = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "huawei",
    "appPackage":"com.lemon.lemonban",
    "appActivity":"com.lemon.lemonban.activity.WelcomeActivity",
    "noReset":True

}

# 跟appium建立连接，然后再把启动参数发过去。
webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

# 执行时，请保证：1 设备在线  2、appium server已启动