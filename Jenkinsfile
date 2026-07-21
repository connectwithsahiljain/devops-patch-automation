pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                echo 'Repo clone successful'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Python') {
            steps {
                bat 'python hello.py'
            }
        }
    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }    
    }
}