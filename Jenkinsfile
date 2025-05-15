pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/savitskiy1995/python-jenkins'  // Укажите ваш репозиторий
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'  // Убедитесь, что у вас есть файл requirements.txt
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --html=report.html'  // Запуск тестов с генерацией HTML-отчета
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: false,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'HTML Report'
                ])
            }
        }
    }
}