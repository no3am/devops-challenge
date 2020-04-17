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
                sh 'pip install -r requirements.txt'
                sh 'python3 test_hello_world.py > test-reports/results.xml'
            }
        }
    }
}