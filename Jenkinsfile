pipeline {
    agent any

    stages {
        stage('Send Mail') {
            steps {
                bat 'python mail.py'
            }
        }
    }
}
