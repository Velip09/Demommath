Usage of the Demommath Package
==============================

Installation
------------

.. code-block:: python
	:linenos:

    	pip install demommath

.. _How to use the commands:

Using the commands
------------------

**To call the functions by specifying their directory (These functions are imported in the __init__.py files of the respective directories):**

## Usage for adding numbers

.. code-block:: python
	:linenos:
 
  	from demommath import addsub
  	addsub.add(2,8)
  	10

## Usage for subtracting numbers

.. code-block:: python
	:linenos:

	from demommath import addsub
	addsub.subtract(3,5)
	-2

## Usage for multiplying numbers

.. code-block:: python
	:linenos:

	from demommath import multidiv
	multidiv.multiply(4,9)
	36

## Usage for dividing numbers

.. code-block:: python
	:linenos:

	from demommath import multidiv
	multidiv.divide(5,4)
	1.25

## Usage for identifying odd and even numbers

.. code-block:: python
	:linenos:

	from demommath import odd_even
	odd_even.is_odd_or_even(6)
	'Even'

##  Usage for finding LCM of 3 numbers

.. code-block:: python
	:linenos:

	from demommath import calculations
	calculations.lcm(5,7,8)
	280

##  Usage for finding mean of a list of numbers

.. code-block:: python
	:linenos:

	from demommath import calculations
	calculations.find_mean([4,6,7,3,5])
	5.0

## Usage for identifying prime numbers

.. code-block:: python
	:linenos:

	from demommath import prime_num
	prime_num.is_prime(5)
	True

## Usage for adding arrays

.. code-block:: python
	:linenos:

	from demommath import sumarray
	sumarray.add_num([5,6,7],[4,3,2])
	array([9, 9, 9])

**To call the default functions (These functions are imported in the __init__.py file in the main directory):**

## Usage for adding numbers

.. code-block:: python
	:linenos:

	import demommath as dmaddsub
	dm.add(5,6)
	11

## Usage for subtracting numbers

.. code-block:: python
	:linenos:

	import demommath as dm
	dm.subtract(5,6)
	-1

##  Usage for finding LCM of 3 numbers

.. code-block:: python
	:linenos:

	import demommath as dm
	dm.lcm(5,7,8)
	280

##  Usage for finding mean of a list of numbers

.. code-block:: python
	:linenos:

	import demommath as dm
	dm.find_mean([4,6,7,3,5])
	5.0

**To call the functions directly (These functions are defined in the __all__ list in the __init__.py file of the main directory):**

## Usage for adding numbers

.. code-block:: python
	:linenos:

	from demommath import *
	add(3,6)
	9

##  Usage for finding LCM of 3 numbers

.. code-block:: python
	:linenos:

	from demommath import *
	lcm(5,7,8)
	280

##  Usage for finding mean of a list of numbers

.. code-block:: python
	:linenos:

	from demommath import *
	find_mean([4,6,7,3,5])
	5.0
