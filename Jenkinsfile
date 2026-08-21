pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\ELCOT\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/singathurai007/bytezera-devops.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON%" -m pip install -r requirements.txt'
            }
        }

        stage('Test FastAPI') {
    steps {
        bat '"%PYTHON%" -c "from app.main import app; print(app)"'
        bat 'curl -f http://127.0.0.1:8000/health'
    }
}

        stage('Deploy') {
            steps {
                bat 'echo FastAPI deployment completed'
            }
        }
    }
}
