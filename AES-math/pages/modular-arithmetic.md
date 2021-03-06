#### Modular arithmetic, briefly

Modular arithmetic is all of

- addition
- multiplication
- subtraction
- division

with integers, *modulo* (or mod) some integer *n*. 

Here is an addition table for n = 4

```
    0  1  2  3  
   ------------
0 | 0  1  2  3
1 | 1  2  3  0
2 | 2  3  0  1
3 | 3  0  1  2
```

Example:  ``3 + 2 = 5 % 4 = 1``.

The rule is to keep the remainder after dividing by the modulus.  Since ``36/7 = 1`` and ``15/7 = 1``

```
1 = 8 = 15 = 22 = 29 = 36 (mod 7) ...
```

#### Multiplication

Consider **multiplication** mod ``n = 6`` and ``n = 7``:

```
  6
  1  |  0  1  2  3  4  5
  2  |  0  2  4  0  2  4
  3  |  0  3  0  3  0  3
  4  |  0  4  2  0  4  2
  5  |  0  5  4  3  2  1

  7
  1  |  0  1  2  3  4  5  6
  2  |  0  2  4  6  1  3  5
  3  |  0  3  6  2  5  1  4
  4  |  0  4  1  5  2  6  3
  5  |  0  5  3  1  6  4  2
  6  |  0  6  5  4  3  2  1
```

For n = 6, *only* the rows with multiplications of 1 and 5 generated all the integers less than 6.  This is a common pattern, it's always true that 1 and n-1 generate all the values < n.  That's because

```
x*1 + x*(n-1) = 0 (mod n)
```

and *that's* because

```
x*1 + x*(n-1) = x + nx - x = nx = 0 (mod n)
```

**Important**:

Since all integers < n are generated from each starting integer in the special case, a unique result must be produced for each multiplication.

For n = 7, *every* number generated all the other ones.

If a number, multiplied by all the elements of the field generates all the elements of the field, then at least one of those results must be equal to 1.  

The two multiplicands with this property are called multiplicative inverses. 

Each row contains all possible values < n if n is prime.  See [mod.py](code/mod1.py).

#### co-primes

The most interesting cases are those where n is not prime, yet certain integers other than 1 and n-1 generate all the integers < n.  

It turns out that this happens when the smaller number is co-prime with n (they have no common factors other than 1).

So for example, here is the multiplication table for n = 8 where all integers < 8 are generated by 3 and 5:

```
8
  1  |  0  1  2  3  4  5  6  7
  2  |  0  2  4  6  0  2  4  6
  3  |  0  3  6  1  4  7  2  5
  4  |  0  4  0  4  0  4  0  4
  5  |  0  5  2  7  4  1  6  3
  6  |  0  6  4  2  0  6  4  2
  7  |  0  7  6  5  4  3  2  1
```

6 is not co-prime to 8 because they share the common factor 2, whereas 3 and 5 are co-prime.  Here, both 3 and 5 are their own multiplicative inverses.

#### Powers

With n = 7, consider the **powers** of each i < 7:

```
    1  2  3  4  5  6
   ---------------------
1 | 1  1  1  1  1  1
2 | 2  4  1  2  4  1
3 | 3  2  6  4  5  1
4 | 4  2  1  4  2  1
5 | 5  4  6  2  3  1  
6 | 6  1  6  1  6  1
```

This table can be a challenge to construct.  I wrote a script to help with the calculations the first time through. 

Looking at the table, we discover that the powers of 3 and 5 (but not 2,4,6) give all the integers less than 7.  

These two (but not only these two) have the property that

- 3<sup>n-1</sup> = 3<sup>6</sup> = 1
- 3<sup>n</sup> = 3
- 5<sup>n-1</sup> = 5<sup>6</sup> = 1
- 5<sup>n</sup> = 5


#### Take the modulus at each step

A big simplification for calculation is to take the modulus at each step.  This keeps the numbers small and it works because if ``z = x * y`` then

```
z % n = (x % n) * (y % n)
```

Every integer is equal to an integer quotient ``Q`` + a remainder ``R < n``.  So

```
x = q_x + r_x
y = q_y + r_y
x * y = q_x * q_y + q_x * r_y +
        q_x * r_x + r_x * r_y
```

The only term on the right which is not evenly divisible by ``n`` is the last one (the others all have a factor ``q``).  Thus

```
(x * y) % n = (r_x * r_y) % n
```

So, for example 

```5^2 = 25 = 4 mod 7``` 

and 

```5^4 = (5^2)^2 = 4^2 = 2 (mod 7)```

In the row:

```
5 | 5  4  6  2  3  1  
```

The value at position 5 is equal to the product of the values at positions 2 and 3:  4 x 6 = 24 = 3 (mod 7).

#### Division

Consider multiplication mod n = 7 again:

```
  7
  1  |  0  1  2  3  4  5  6
  2  |  0  2  4  6  1  3  5
  3  |  0  3  6  2  5  1  4
  4  |  0  4  1  5  2  6  3
  5  |  0  5  3  1  6  4  2
  6  |  0  6  5  4  3  2  1
```

Since ``2 * 4 = 1 (mod 7)``, 4 and 2 are multiplicative inverses, similarly ``3,5`` and ``6,6`` as well as ``1,1``.  This allows us to define division by q as the same as multiplication by the multiplicative inverse of q.

So

```
5 / 4 = 2 * 5 = 3 (mod 7)
```
