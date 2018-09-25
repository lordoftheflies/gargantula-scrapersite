pipeline {
    agent any

    environment {
        REPOSITORY_NAME = 'gargantula-scrapersite'
        PYTHON_MODULE_NAME = 'scrapersite'
        PYTHON_PATH = '/usr/bin/python3.6'
        VIRTUAL_ENVIRONMENT_NAME = 'env'
        PYPI_EXTRA_INDEX_URL = 'https://pypi.cherubits.hu'
        PYPI_REPOSITORY = 'local'
        DOTENV_PATH = '~/.gargantula'
    }

    stages {
        stage('SCM') {
            steps {
                slackSend channel: "#jenkins", message: "Build #${env.BUILD_NUMBER} Started - ${env.JOB_NAME} (<${env.BUILD_URL}|Open>)"

                git(url: "git@github.com:lordoftheflies/${REPOSITORY_NAME}.git", branch: 'master', changelog: true, credentialsId: 'credentials-github-lordoftheflies-ssh', poll: true)
            }
        }

        stage('Install virtual environment') {
            steps {
                sh '''if [ ! -d "${VIRTUAL_ENVIRONMENT_NAME}" ]; then
                    virtualenv --no-site-packages -p ${PYTHON_PATH} ${VIRTUAL_ENVIRONMENT_NAME}
                fi'''
            }
        }

        stage('Setup dotenv') {
            steps {
                fileOperations([
                    fileDeleteOperation(file: "${HOME}/.gargantula"),
                    fileCopyOperation(excludes: '', flattenFiles: true, includes: 'env.template', targetLocation: "${HOME}"),
                    fileRenameOperation(source: "${HOME}/env.template", destination: "${HOME}/.gargantula")
                ])

                sh '''if [ ! -f "${HOME}/.gargantula" ]; then
                    sed -i -- 's/DEVELOPMENT/STAGING/g' "${HOME}/.gargantula"
                fi'''
            }
        }

        stage('Setup') {
            steps {
                sh '''. ./${VIRTUAL_ENVIRONMENT_NAME}/bin/activate
                    pip install -r requirements.txt --extra-index-url=${PYPI_EXTRA_INDEX_URL}
                    python manage.py collectstatic --noinput
                    python manage.py migrate
                deactivate'''
            }
        }

        stage('Cleanup') {
            steps {
                sh '''. ./${VIRTUAL_ENVIRONMENT_NAME}/bin/activate
                    if [ -d "dist" ]; then
                        rm -r dist
                    fi
                deactivate'''
            }
        }

        stage('Test') {
            steps {
                sh '''. ./${VIRTUAL_ENVIRONMENT_NAME}/bin/activate
                    pytest --verbose --junit-xml test-reports/results.xml
                deactivate'''
            }
            post {
                always {
                    // Archive unit tests for the future
                    junit allowEmptyResults: true, testResults: 'test-reports/results.xml'
                }
            }
        }

        stage('Static code metrics') {
            steps {
                echo "Code Coverage"
                sh  ''' . ./${VIRTUAL_ENVIRONMENT_NAME}/bin/activate
                        coverage run --source='.' manage.py test ${PYTHON_MODULE_NAME}
                        python -m coverage xml -o ./test-reports/coverage.xml

                    '''
                echo "PEP8 style check"
                sh  ''' . ./${VIRTUAL_ENVIRONMENT_NAME}/bin/activate
                        pylint --disable=C ${PYTHON_MODULE_NAME} || true
                    '''
            }

            post{
                always{
                    step([$class: 'CoberturaPublisher',
                                   autoUpdateHealth: false,
                                   autoUpdateStability: false,
                                   coberturaReportFile: 'test-reports/coverage.xml',
                                   failNoReports: false,
                                   failUnhealthy: false,
                                   failUnstable: false,
                                   maxNumberOfBuilds: 10,
                                   onlyStable: false,
                                   sourceEncoding: 'ASCII',
                                   zoomCoverageChart: false])
                }
            }
        }

        stage('Update version') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                sh '''. ./${VIRTUAL_ENVIRONMENT_NAME}/bin/activate
                    BUMPED_VERSION=$(cat ${PYTHON_MODULE_NAME}/version.py | grep "__version__ = " | sed 's/__version__ =//' | tr -d "'")
                    echo "$BUMPED_VERSION"
                    bumpversion --allow-dirty --message 'Jenkins Build {$BUILD_NUMBER} bump version of ${REPOSITORY_NAME}: {current_version} -> {new_version}' --commit --tag --tag-name 'v{new_version}' --current-version $BUMPED_VERSION patch ${PYTHON_MODULE_NAME}/version.py
                deactivate'''

                sh '''git push origin master'''
            }
        }

        stage('Build') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                sh '''. ./${VIRTUAL_ENVIRONMENT_NAME}/bin/activate
                    python setup.py sdist develop
                deactivate'''
            }
        }

        stage('Deploy staging') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                sh '''. ./${VIRTUAL_ENVIRONMENT_NAME}/bin/activate
                    python setup.py sdist install
                deactivate'''
            }
        }

        stage('Distribute') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                script {
                    try {
                        sh '''. ./${VIRTUAL_ENVIRONMENT_NAME}/bin/activate
                            twine upload -r ${PYPI_REPOSITORY} dist/*
                        deactivate'''
                    } catch(error) {
                        echo 'Deploy failed.'
                        echo 'Exception in distribution: ${error}.'
                        echo currentBuild.result
                    }

                    slackSend color: "warning", channel: "#jenkins", message: "Build #${env.BUILD_NUMBER} Deployment Completed - ${env.JOB_NAME} (<https://jenkins.cherubits.hu/blue/organizations/jenkins/${REPOSITORY_NAME}/detail/master/${env.BUILD_NUMBER}/pipeline|Open>, <https://pypi.cherubits.hu/packages/|Show>)"
                }
            }
        }

    }

    post {
        success {
            slackSend color: "good", channel: "#jenkins", message: "Build #${env.BUILD_NUMBER} Succeed - ${env.JOB_NAME} (<https://jenkins.cherubits.hu/blue/organizations/jenkins/gargantula-frontend/detail/master/${env.BUILD_NUMBER}/pipeline|Open>)"
        }

        failure {
            slackSend color: "danger", channel: "#jenkins", message: "Build #${env.BUILD_NUMBER} Failed - ${env.JOB_NAME} (<https://jenkins.cherubits.hu/blue/organizations/jenkins/gargantula-frontend/detail/master/${env.BUILD_NUMBER}/pipeline|Open>)"
        }
    }
}