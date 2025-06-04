# Дипломная работа SB1 "Доска объявлений

### Установка Docker на сервер (Ubuntu 20.04)
1. Установите необходимые пакеты
```shell
     sudo apt update
     sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
2. Добавьте GPG ключ Docker
```shell
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
3. Добавьте репозиторий Docker
```shell
   echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
4. Установите Docker
```shell
   sudo apt update
   sudo apt install docker-ce docker-ce-cli containerd.io
```
5. Добавьте своего пользователя в группу docker
```shell
    sudo usermod -aG docker $USER
```
6. Перезапустите Docker
```shell
    sudo systemctl restart docker
```

## !!!ВНИМАНИЕ!!! ##
### Инструкция перед запуском проекта (порядок выполнения имеет значение)

1. Перед запуском проекта переименуйте файл [.env.example](.env) в `.env` и поменяйте содержимое на свои переменные окружения
2. Выполните команду
```shell
   docker-compose up -d --build
```

После запуска веб-приложение будет доступно по адресу: http://localhost:8000

**Дополнительные команды:**
- Для просмотра запущенных контейнеров:
```shell
  docker-compose ps
```
Для просмотра логов всех контейнеров:
```shell
  docker-compose logs
```
- Для остановки сервисов:
```shell
  docker-compose down
```