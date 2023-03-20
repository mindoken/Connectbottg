import logging
from run import Run


logging.basicConfig( #базовые настройки конфигурации
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    Run() #запуск метода, который активирует систему
