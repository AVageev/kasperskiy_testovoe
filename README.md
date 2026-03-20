# Report Service  

API для анализа текстовых файлов и построения частотной статистики словоформ.  

## Стек  
Python 3.10+  
FastAPI  
openpyxl  
pymorphy3  

## Среда разработки  
Linux Ubuntu 22.04  

## Установка и запуск  

```bash  
1. Создать виртуальное окружение  
python3 -m venv venv  
2. Запустить виртуальное окружение  
Linux/macOS:  
source venv/bin/activate  
Windows:  
venv\Scripts\activate  
3. Установить зависимости:  
pip install -r requirements.txt  
4. Запустить сервер:  
uvicorn app.main:app --reload  
```
5. Открыть Swagger для тестирования:  
http://127.0.0.1:8000/docs  


## Endpoint  
POST /public/report/export  
Принимает .txt файл  
Возвращает JSON:  
{"status": "processing"}  
Генерирует report.xlsx в корне проекта  

## Контакты  
Telegram: @AndreyAgEEvf  
Почта: andrey.ageev.04@gmail.com  
