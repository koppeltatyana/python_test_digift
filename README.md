# python_test_digift

## Генерация отчетов в Allure
1. Из виртуального окружения запускаем скрипт 'py.test --alluredir allure-results tests\test_ui.py'
![изображение](https://user-images.githubusercontent.com/25736580/150678983-5a0da6c4-82d5-4150-90e2-9d01909e782d.png)

2. После успешного прохождения теста, запускаем скрипт 'D:\Python\allure-2.17.2\bin\allure.bat generate allure-results' для генерации отчета => отчет сгенерирован
![изображение](https://user-images.githubusercontent.com/25736580/150679032-59f1581d-5648-4ee5-b9e7-f18c8004696e.png)

3. Открываем сгенерированный отчет скриптом 'D:\Python\allure-2.17.2\bin\allure.bat open allure-report' => открывается страница http://192.168.0.103:59166/index.html
![изображение](https://user-images.githubusercontent.com/25736580/150679118-f9678bdb-d9a8-42ad-ae43-af1a9b1b90be.png)

![изображение](https://user-images.githubusercontent.com/25736580/150679166-1c3f4e02-76d7-4af1-b308-8d7d2f5669f2.png)
(папки allure-report и allure-results не были добавлены на гит в целях чистоты остального кода репозитория)
