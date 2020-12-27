**README**

> This CLI provides access to a pizza restaurant keeper.

**INSTALLATION**
>**Conda**   
>Run to create virtual env:   
`conda env create -n pizza_env -f conda_config.yml`   
`conda activate pizza_env`

**USAGE**   
>General usage:   
`python pizza_cli.py order PIZZA_NAME`

>To order pizza Pepperoni without delivery and then pick-up in a restaraunt:   
`python pizza_cli.py order Pepperoni`

>To order pizza Hawaiian with delivery:   
`python pizza_cli.py order Hawaiian --delivery`

**TESTING**
>Tests are performed using pytest framework.   
>Please check test_pizza_cli.py and test_pizza.py