# ndm
Для проверки работоспособности нужно:
1) выполнить команду gh repo clone DzoT1999-sys/ndm
2) перейти в склонированный репозиторий cd /<путь в вашей системе>/ndm
3) запустить сборку в докере docker compose up -d --build
4) выполнять проверку курлами созданного стенда

Результаты выполнения на тестовом стенде

Тест 1: Прямой запрос (1 прокси)
JVHHQW4JR7:ndm shmatin.andrey$ curl -s http://localhost:8081/ | python3 -m json.tool
{
    "X-Forwarded-For": "192.168.65.1"
}

Тест 2: Попытка спуфинга заголовка
JVHHQW4JR7:ndm shmatin.andrey$ curl -s -H "X-Forwarded-For: 1.2.3.4" http://localhost:8081/ | python3 -m json.tool
{
    "X-Forwarded-For": "192.168.65.1"
}

Тест 3: Цепочка nginx1 → nginx2 → app
JVHHQW4JR7:ndm shmatin.andrey$ curl -s http://localhost:8081/via2 | python3 -m json.tool
{
    "X-Forwarded-For": "192.168.65.1, 172.20.0.5"
}

Тест 4: Цепочка nginx1 → nginx2 → nginx3 → app + спуфинг
JVHHQW4JR7:ndm shmatin.andrey$ curl -s -H "X-Forwarded-For: 9.9.9.9" http://localhost:8081/via3 | python3 -m json.tool
{
    "X-Forwarded-For": "192.168.65.1, 172.20.0.5, 172.20.0.4"
}

Тест 5: Вход через nginx2 (альтернативная точка входа)
JVHHQW4JR7:ndm shmatin.andrey$ curl -s -H "X-Forwarded-For: 5.5.5.5" http://localhost:8082/ | python3 -m json.tool
{
    "X-Forwarded-For": "192.168.65.1"
}
