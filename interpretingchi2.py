"""
Interpreting Chi^2
Author: Sheila Kannappan
excerpted/adapted from CAP REU tutorial September 2016
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr

# experiment to illustrate Monte Carlo creation of chi^2 
# distributions for two values of N

#i=0
#if i == 0:
for i in xrange(2):

  narr=30*(1+9*i) #30 first time, 300 second time
  chisqs=[]
  iters=1000  # experiment with rerunning the plots many times
             # to see how the random variations change the chi^2
             # start w/ iters=100 then change iters to 1000 and repeat

  for j in xrange(iters):
    # create a data set with random errors whose underlying
    # functional form is y=1/x
    xvals = np.zeros(narr)
    yvals = np.zeros(narr)
    xvals = np.arange(narr)/(1.+9.*i) + 1.
    errs=0.1
    yvals = 1./xvals + npr.normal(0,errs,narr)
    # what does npr.normal do?
    #It adds a certain amount of error to our "measurements" because in the
    #real world we may not know what that error might be, but we might know
    #it falls within a certain confidence interval.

    resids = np.abs(yvals - 1./xvals)
    # why are we subtracting 1./xvals?
    # because 1./xvals represents our expected values and the residual is
    #defined by the [(observed value)-(expected value)].

    chisq = np.sum(resids**2 / errs**2)
    # roughly, how is chisq related to N?
    #chisq is approximately equal to N, and in this case N is equal to the
    #number of data points because there are no free parameters.

    # what if we didn't know the errors and overestimated
    # them as 0.2 -- how would chi^2 change?
    #chi^2 would decrease if we increased errs to 0.2 which would make it look
    #as if the reduced chi^2 had a better fit.

    chisqs.append(chisq) # building up iters trial values of chi^2
    
  if i==0:
      redchisqdist1 = np.array(chisqs)/narr
      # compute array of "reduced chi^2" values found for 1st N
      # what does "reduced" mean? why are we dividing by narr?
      #"Reduced" chi^2 is a way of determining if a model is a good fit.
      #We are dividing by narr because in this model y=1/x has no free parameters,
      #so N=narr, or the number of data points.

  if i==1:
      redchisqdist2 = np.array(chisqs)/narr
      # same thing for 2nd N 
      
plt.figure(2)
plt.clf()
n1, bins1, patches1 = plt.hist(redchisqdist1,bins=0.05*iters,normed=1,histtype='stepfilled')
n2, bins2, patches2 = plt.hist(redchisqdist2,bins=0.05*iters,normed=1,histtype='step')
plt.setp(patches1,'facecolor','g','alpha',0.75)
plt.xlim(0,2.5)
plt.setp(patches2,'hatch','///','alpha',0.75,color='blue')
# what good plotting strategies are being used here?
#When overplotting the 2nd plot, N=300, the histogram was made such that it is hatched so you can
#still see the first, N=30, plot beneath it. They are also labeled well so you can easily distinguish
#between which plot represents which set of data.

plt.title('comparison of reduced chi-squared distributions')
#plt.title('reduced chi-squared distribution') 
# switch titles above when you add N=300 case

plt.text(1.4,1,"N=30",size=11,color='g')
plt.text(1.2,3,"N=300",size=11,color='b')

# Q: how can we determine the confidence level associated with
#    a certain deviation of reduced chi^2 from 1?
# A: we have to do the integral under the distribution --
#    e.g. for 3sigma (99.8%) confidence find x such that
#    the integral up to x contains 99.8% of the area
# how can you approximate this using np.argsort?
#This can be approximated by using np.argsort to sort the data such that indices
#assigned to each red chi^2 will be listed from least to greatest. Then we use the
#998 element from the array inds, that is inds[998] that correspondes to the 99.8% 
#confidence interval. The output of inds[998] will be the element we have to search
#for in redchisqdist1[inds[998]] & redchisqdist2[inds[998]] to obtain the reduced
#chi^2 for 99.8% confidence for both N=30 and N=300.
# make sure to set iters=1000 for this exercise....
inds=np.argsort(redchisqdist1)
print("Reduced chi^2 for 99.8% confidence for N=30:", redchisqdist1[inds[998]]) # fill in to print red. chi^2 for 99.8% conf. for N=30
inds=np.argsort(redchisqdist2)
print('Reduced chi^2 for 99.8% confidence for N=300:', redchisqdist2[inds[998]]) # fill in to print red. chi^2 for 99.8% conf. for N=300
# look at the graph and verify your answers make visual sense
