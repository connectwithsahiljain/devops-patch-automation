// pipeline {
//     agent any

//     stages {
//         stage('checkout') {
//             steps {
//                 echo 'Repo clone successful'
//             }
//         }

//         stage('Install Dependencies') {
//             steps {
//                 bat 'pip install -r requirement.txt'
//             }
//         }

//         stage('Run Python') {
//             steps {
//                 bat 'python hello.py'
//             }
//         }
//     }    
//     post {
//         success {
//             echo 'Pipeline completed successfully.'
//         }
//         failure {
//             echo 'Pipeline failed.'
//         }
//     }    
// }



// node{    
//     stage('checkout'){
//         checkout scm
//     }

//     stage('Run Python'){
//         bat 'python hello.py'
//     }

//     stage('Complete'){
//         echo 'Pipeline completed successfully.'
//     }
// }

pipeline{
    agent any

    stages{
        stage('Use Credentials'){
            steps{
                withCredentials([string(credentialsId: 'demo', variable: 'MY_SECRET')]){
                    // Your steps that use the credentials go here
                    bat "echo %MY_SECRET%"
                }
            }
        }
    }
}


