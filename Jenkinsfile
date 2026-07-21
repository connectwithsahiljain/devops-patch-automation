pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                echo 'Repo clone successful'
            }
        }

        stage('Run Python') {
            steps {
                bat 'python hello.py'
            }
        }
    }
}