pipeline {
		environment {
    PATH = "C:\\Program Files\\Git\\usr\\bin;C:\\Program Files\\Git\\bin;${env.PATH}"
    agent any
    stages {
        stage('build') {
            steps {
                bat 'python Hello2.py'
            }
        }
    }
}
}