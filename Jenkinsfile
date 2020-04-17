pipeline {
    agent { docker { image 'python:3.7.2' } }
    stages {
        stage('Build') {
            steps {
                sh 'python -m py_compile hello.py hello.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
        stage('Test') {
            steps {
                sh 'pip install -r Flask==1.0.2'
                sh 'py.test --junit-xml test-reports/results.xml test_hello_world.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}