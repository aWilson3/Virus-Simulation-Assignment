# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    TimeSteps = [300,150,75,0]
    viruses = []
    for i in range(100):
        viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol':False}, 0.005))
    w=1
    for step in TimeSteps:
        VirusPop = []
        for i in range(step+150):
            VirusPop.append(0)
        for j in range(numTrials):
            person = TreatedPatient(viruses, 1000)
            for k in range(step):
                VirusPop[k] += person.update()
            person.addPrescription('guttagonol')
            for l in range(step,step+150):
                VirusPop[l] += person.update()
        
        pylab.figure(w)
        pylab.hist(VirusPop, bins=25)
        pylab.xlabel('End Population')
        pylab.ylabel('Frequency')
        pylab.title('Virus Population Over Time ' + str(w))
        w += 1


            





#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    TimeSteps = [300,150,75,0]
    viruses = []
    for i in range(100):
        viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol':False,'grimpex':False}, 0.005))
    w=1
    for step in TimeSteps:
        VirusPop = []
        for i in range(step+300):
            VirusPop.append(0)
        for j in range(numTrials):
            person = TreatedPatient(viruses, 1000)
            for k in range(150):
                VirusPop[k] += person.update()
            person.addPrescription('guttagonol')
            for l in range(150,step+150):
                VirusPop[l] += person.update()
            person.addPrescription('grimpex')
            for g in range(step+150, step+300):
                VirusPop[g] += person.update()
        
        pylab.figure(w)
        pylab.hist(VirusPop, bins=25)
        pylab.xlabel('End Population')
        pylab.ylabel('Frequency')
        pylab.title('Virus Population Over Time ' + str(w))
        w += 1

