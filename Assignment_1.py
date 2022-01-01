{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bdc26e9d",
   "metadata": {},
   "source": [
    "# Question No 1\n",
    "### Write a Python program to write following string in a specific format(see thee output).\n",
    "### Twinkle, twinkle, Iittle star, How I wonder what you are Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, Iittle star, How I wonder what you are."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d39cd1cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Twinkle, twinkle, little star, \n",
      "\tHow I wonder what you are! \n",
      "\t\tUp above the world so high, \n",
      "\t\tLike a diamond in the sky. \n",
      "Twinkle, twinkle, little star, \n",
      "\tHow I wonder what you are!\n"
     ]
    }
   ],
   "source": [
    "print(\"Twinkle, twinkle, little star, \\n\\tHow I wonder what you are! \\n\\t\\tUp above the world so high, \\n\\t\\tLike a diamond in the sky. \\nTwinkle, twinkle, little star, \\n\\tHow I wonder what you are!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d7d8144a",
   "metadata": {},
   "source": [
    "# Question No 2\n",
    "### Write a Python program to get the Python version you ae using.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0c4685f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python version\n",
      "3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)]\n",
      "Version info.\n",
      "sys.version_info(major=3, minor=8, micro=8, releaselevel='final', serial=0)\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "print(\"Python version\")\n",
    "print (sys.version)\n",
    "print(\"Version info.\")\n",
    "print (sys.version_info)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "25ad8d65",
   "metadata": {},
   "source": [
    "# Question No 3\n",
    "### Write a Python program to display the current dae and time.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "958a06b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Current date and time : \n",
      "2022-01-01 15:13:18\n"
     ]
    }
   ],
   "source": [
    "import datetime\n",
    "now = datetime.datetime.now()\n",
    "print (\"Current date and time : \")\n",
    "print (now.strftime(\"%Y-%m-%d %H:%M:%S\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "05ee1ea8",
   "metadata": {},
   "source": [
    "# Question No 4\n",
    "### Write a Python program which accepts the radlus of a circle from the user and compute the area."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c59cb6bb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input the radius of the circle : 2\n",
      "The area of the circle with radius 2.0 is: 12.566370614359172\n"
     ]
    }
   ],
   "source": [
    "from math import pi\n",
    "r = float(input (\"Input the radius of the circle : \"))\n",
    "print (\"The area of the circle with radius \" + str(r) + \" is: \" + str(pi * r**2))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f2332357",
   "metadata": {},
   "source": [
    "# Question No 5\n",
    "### Write a Python program which acoepts the users first and last name and print them in revese order with a space between them."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "3e6818c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input your First Name : Muhammad\n",
      "Input your Last Name : Adnan\n",
      "Hello  Adnan Muhammad\n"
     ]
    }
   ],
   "source": [
    "firstName = input(\"Input your First Name : \")\n",
    "lastName = input(\"Input your Last Name : \")\n",
    "print (\"Hello  \" + lastName + \" \" + firstName)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f958bf71",
   "metadata": {},
   "source": [
    "# Question No 6\n",
    "### Write a python program which takes two inputs from user and print them addition."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "913d24e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type a number: 2\n",
      "Type another number: 5\n",
      "The sum is:  7\n"
     ]
    }
   ],
   "source": [
    "x = input(\"Type a number: \")\n",
    "y = input(\"Type another number: \")\n",
    "\n",
    "sum = int(x) + int(y)\n",
    "\n",
    "print(\"The sum is: \", sum)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
