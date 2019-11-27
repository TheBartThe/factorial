pipeline{
	
	agent any
	stages{
		stage("-----create init-----") {
			steps{
				sh "touch ./factorial/__init__.py"
				sh "touch ./factorialTests/__init__.py"
			}
		}
		
		stage("-----testing-----") {
			steps{
				sh "pytest factorialTests/factorial_test.py"
			}
		}
	}
}
