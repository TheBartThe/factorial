pipeline{
	
	agent any
	stages{
		stage("-----create init-----") {
			steps{
				sh "touch __init__.py factorial"
				sh "touch __init__.py factorialTests"
			}
		}
		
		stage("-----testing-----") {
			steps{
				sh "pytest factorialTests/factorial_test.py"
			}
		}
	}
}
