from math import gcd
from operator import truediv

from win32gui import FlashWindowEx


class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self,num: int=0, den: int=1):
        """This builds a fraction based on some numerator and denominator.

        PRE :
        - `num` est un entier.
        - `den` est un entier différent de 0.

        POST :
            - Une instance de Fraction est créée.
            - La fraction est automatiquement simplifiée.
            - Le dénominateur est toujours positif.

        Raises:
            ZeroDivisionError: Si `den` est nul.
        """
        if den == 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être zéro.")
        self._numerator= num
        self._den= den


        pgcd = gcd(num, den)
        self._numerator = num // pgcd * (-1 if den < 0 else 1)
        self._den = abs(den) // pgcd



    @property
    def numerator(self) -> int:
        return self._numerator

    @property
    def denominator(self) -> int:
        return self._den

    # ------------------ Textual representations ------------------

    def __str__(self) -> str:
        """Return a textual representation of the reduced form of the fraction

        PRE : -
        POST : return une chaîne de caractères sous forme "numerator/denomirator"
        """
        return f"{self.numerator}/{self._den}" #if self._den!=1 else f"{self.numerator}"

    def as_mixed_number(self) -> str:
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : -
        POST : return une chaine de caractère :
                - si numerator > den : retourne "entier + (numerator%den)/den"
                - sinon : return la fraction simplifiée.
        """
        reste = self.numerator%self.denominator
        integer = self.numerator // self.denominator

        if reste == 0:
            return str(integer)

        if abs(self.numerator) > abs(self.denominator)  :
            return f"{integer} + {abs(reste)}/{abs(self.denominator)}"




        return f"{self.numerator}/{self.denominator}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """Overloading of the + operator for fractions

        PRE : -.
        POST : retourne une fraction représentant la somme des deux fractions sous forme simplifiée.
        Raises:
            TypeError: Si other n'est pas une instance de Fraction.
         """
        if not isinstance(other, Fraction):
            raise TypeError("Valeur invalide")
        num = (self.numerator* other.denominator) + (other.numerator*self.denominator)
        den= (self.denominator*other.denominator)


        return Fraction(num,den) # if den=1 else num



    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """Overloading of the - operator for fractions

        PRE : -
        POST : retourne une fraction représentant la différence des deux fractions sous forme simplifiée.
        Raises:
            TypeError: Si other n'est pas une instance de Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Valeur invalide")
        num = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        den = (self.denominator * other.denominator)

        return Fraction(num,den)



    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """Overloading of the * operator for fractions

        PRE : -
        POST : retourne une nouvelles frction  simplifiée , résultat de la multiplication de ces deux fractions( self et other)
        Raises:
            TypeError: other n'est pas une instance de Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Valeur invalide")
        num = self.numerator *other.numerator
        den = self.denominator * other.denominator



        return Fraction(num,den)


    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """Overloading of the / operator for fractions

        PRE : -
        POST : retourne une forme simplifiée de la division de ces deux fractions( self et other)
        Raises:
            TypeError: Si other n'est pas une instance de Fraction.
            ZeroDivisionError: le numérateur de la fraction divisante est nulle.
        """
        if  not isinstance(other,Fraction):
            raise TypeError("Valeur invalide")

        if other.numerator ==0:
            raise ZeroDivisionError("le numérateur de la fraction divisante ne doit pas être zéro")

        num=self.numerator*other.denominator
        den= self.denominator*other.numerator

        return Fraction(num,den)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : -
        POST : retourne une forme simplifiée de self élevé à la puissance 'other'
        Raises:
            TypeError: Si other n'est pas une instance de Fraction.
        """
        if  not isinstance(other,Fraction):
            raise TypeError("Valeur invalide")

        if not isinstance(other, Fraction):
            raise TypeError("Valeur invalide")
        if other.numerator == 0:
            return Fraction(1,1)
        if other.numerator < 0 or other.denomintor < 0:
            num = self.denominator ** abs(other)
            den= self.numerator ** abs(other)

        else:
            num =self.numerator ** other
            den= self.denominator ** other



        return Fraction(num, den)




    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : -
        POST : retourne True si self et other son équivalentes , False sinon

        Raises:
            TypeError: Si other n'est pas une instance de Fraction.
        """
        if  not isinstance(other,Fraction):
            raise TypeError("Valeur invalide")


        return  self.numerator*other.denominator == other.numerator*self.denominator



    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : -
        POST : - Retourne un nombre flottant correspondant au résultat de la division du numérateur
          par le dénominateur (`self._numerator / self._den`).

        Raises:

            ZeroDivisionError: Si `den` est nul.
        """


        if self._den == 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être zéro.")

        return self.numerator / self.denominator

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking  ------------------

    def is_zero(self) -> bool:
        """Check if a fraction's value is 0

        PRE : -

        POST : return True si cette fraction == 0 , False sinon
        """
        return self.numerator == 0

    def is_integer(self) -> bool:
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : -
        POST : return True si le résultat de cette fraction est un nombre entier , False sinon
        """


        return self.numerator % self.denominator == 0

    def is_proper(self) -> bool:
        """Check if the absolute value of the fraction is < 1
        PRE : -
        POST : return True si le résultat de cette fraction est un nombre propre , False sinon
        """
        return abs(self.numerator) < abs(self.denominator)


    def is_unit(self) -> bool:
        """
        Check if a fraction's numerator is 1 in its reduced form

        PRE : -
        POST : return True si le résultat de cette fraction est égale à 1 , False sinon
        """

        return self.numerator == self.denominator

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : -
        POST : retourne True si les fractions sont adjacentes, False sinon.
        Raises:
            TypeError: Si other n'est pas une instance de Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")

        fraction = self - other

        return abs(fraction.numerator) == 1



