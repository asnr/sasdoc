
/** Does what you want, all the time every time.

 */
%macro foo(a, b, c=, d=default);
data a;
x=1;
        run;
   %mend;
