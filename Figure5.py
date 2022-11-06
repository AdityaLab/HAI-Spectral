import matplotlib.pyplot as plt
import numpy as np
import pickle

if __name__ == '__main__':

    Figure = plt.figure(figsize=(15.36,8.96))

    plt.subplot(2,3,1)

    with open('Data/PreCOVID-Isolation/PreCOVID-Isolation-0.pkl', 'rb') as pkl:       
        cum_new_cases_no, cum_new_cases_rand, cum_new_cases_deg, cum_new_cases_greedy, cum_new_cases_shorr, loads_other_no, loads_other_rand, loads_other_deg, loads_other_greedy, loads_other_shorr, rhos_rand, rhos_deg, rhos_greedy, rhos_shorr = pickle.load(pkl)

    NoMean = []
    RandMean = []
    RandStd = []
    DegMean = []
    DegStd = []
    ShorrMean = []
    ShorrStd = []
    GreedyMean = []
    GreedyStd = []

    for k in range(500,5001,500):
        NoMean.append(np.mean(np.sum(loads_other_no[int((k-500)/500),:,:],axis=1)))
        RandMean.append(np.mean(np.sum(loads_other_rand[int((k-500)/500),:,:],axis=1)))
        RandStd.append(np.std(np.sum(loads_other_rand[int((k-500)/500),:,:],axis=1)))
        DegMean.append(np.mean(np.sum(loads_other_deg[int((k-500)/500),:,:],axis=1)))
        DegStd.append(np.std(np.sum(loads_other_deg[int((k-500)/500),:,:],axis=1)))
        ShorrMean.append(np.mean(np.sum(loads_other_shorr[int((k-500)/500),:,:],axis=1)))
        ShorrStd.append(np.std(np.sum(loads_other_shorr[int((k-500)/500),:,:],axis=1)))
        GreedyMean.append(np.mean(np.sum(loads_other_greedy[int((k-500)/500),:,:],axis=1)))
        GreedyStd.append(np.std(np.sum(loads_other_greedy[int((k-500)/500),:,:],axis=1)))

    RandMean = np.array(RandMean)/np.array(NoMean)
    RandStd = np.array(RandStd)/np.array(NoMean)
    DegMean = np.array(DegMean)/np.array(NoMean)
    DegStd = np.array(DegStd)/np.array(NoMean)
    ShorrMean = np.array(ShorrMean)/np.array(NoMean)
    ShorrStd = np.array(ShorrStd)/np.array(NoMean)
    GreedyMean = np.array(GreedyMean)/np.array(NoMean)
    GreedyStd = np.array(GreedyStd)/np.array(NoMean)

    x1 = np.array(list(range(10))) + 1 - 0.3
    x2 = np.array(list(range(10))) + 1 - 0.1
    x3 = np.array(list(range(10))) + 1 + 0.1
    x4 = np.array(list(range(10))) + 1 + 0.3

    plt.bar(x1,RandMean,yerr=RandStd,capsize=4,color='C7',label='Random',width=0.2)
    plt.bar(x2,DegMean,yerr=DegStd,capsize=4,color='C0',label='Degree',width=0.2)
    plt.bar(x3,ShorrMean,yerr=ShorrStd,capsize=4,color='#6B8E23',label='Shorr',width=0.2)
    plt.bar(x4,GreedyMean,yerr=GreedyStd,capsize=4, color='C3',label='Greedy-Spectral',width=0.2)

    plt.xlabel(r"Budget $k$", fontsize=18)
    plt.ylabel(r"$\gamma_{Loads}$", fontsize=18)
    plt.hlines(1,0.5,10.5,linewidth=1,color='black',linestyle='dashed')
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10],[0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000],fontsize=10)
    plt.yticks([0,0.2,0.4,0.6,0.8,1.0],[0,0.2,0.4,0.6,0.8,1.0],fontsize=12)
    plt.xlim(0.5,10.5)
    plt.ylim(bottom=0,top=1.1)
    plt.title('UVA-PreCOVID',fontsize=14)
    plt.legend(loc=1,fontsize=14)

    plt.subplot(2,3,2)

    with open('Data/PreCOVID-Isolation/PreCOVID-Isolation-0.pkl', 'rb') as pkl:       
        cum_new_cases_no, cum_new_cases_rand, cum_new_cases_deg, cum_new_cases_greedy, cum_new_cases_shorr, loads_other_no, loads_other_rand, loads_other_deg, loads_other_greedy, loads_other_shorr, rhos_rand, rhos_deg, rhos_greedy, rhos_shorr = pickle.load(pkl)

    NoMean = []
    RandMean = []
    RandStd = []
    DegMean = []
    DegStd = []
    ShorrMean = []
    ShorrStd = []
    GreedyMean = []
    GreedyStd = []

    for k in range(500,5001,500):
        NoMean.append(np.mean(cum_new_cases_no[int((k-500)/500),:,-1]))
        RandMean.append(np.mean(cum_new_cases_rand[int((k-500)/500),:,-1]))
        RandStd.append(np.std(cum_new_cases_rand[int((k-500)/500),:,-1]))
        DegMean.append(np.mean(cum_new_cases_deg[int((k-500)/500),:,-1]))
        DegStd.append(np.std(cum_new_cases_deg[int((k-500)/500),:,-1]))
        ShorrMean.append(np.mean(cum_new_cases_shorr[int((k-500)/500),:,-1]))
        ShorrStd.append(np.std(cum_new_cases_shorr[int((k-500)/500),:,-1]))
        GreedyMean.append(np.mean(cum_new_cases_greedy[int((k-500)/500),:,-1]))
        GreedyStd.append(np.std(cum_new_cases_greedy[int((k-500)/500),:,-1]))

    RandMean = np.array(RandMean)/np.array(NoMean)
    RandStd = np.array(RandStd)/np.array(NoMean)
    DegMean = np.array(DegMean)/np.array(NoMean)
    DegStd = np.array(DegStd)/np.array(NoMean)
    ShorrMean = np.array(ShorrMean)/np.array(NoMean)
    ShorrStd = np.array(ShorrStd)/np.array(NoMean)
    GreedyMean = np.array(GreedyMean)/np.array(NoMean)
    GreedyStd = np.array(GreedyStd)/np.array(NoMean)

    x1 = np.array(list(range(10))) + 1 - 0.3
    x2 = np.array(list(range(10))) + 1 - 0.1
    x3 = np.array(list(range(10))) + 1 + 0.1
    x4 = np.array(list(range(10))) + 1 + 0.3

    plt.bar(x1,RandMean,yerr=RandStd,capsize=4,color='C7',label='Random',width=0.2)
    plt.bar(x2,DegMean,yerr=DegStd,capsize=4,color='C0',label='Degree',width=0.2)
    plt.bar(x3,ShorrMean,yerr=ShorrStd,capsize=4,color='#6B8E23',label='Shorr',width=0.2)
    plt.bar(x4,GreedyMean,yerr=GreedyStd,capsize=4, color='C3',label='Greedy-Spectral',width=0.2)

    plt.xlabel(r"Budget $k$", fontsize=18)
    plt.ylabel(r"$\gamma_{Cases}$", fontsize=18)
    plt.hlines(1,0.5,10.5,linewidth=1,color='black',linestyle='dashed')
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10],[0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000],fontsize=10)
    plt.yticks([0,0.2,0.4,0.6,0.8,1.0],[0,0.2,0.4,0.6,0.8,1.0],fontsize=12)
    plt.xlim(0.5,10.5)
    plt.ylim(bottom=0,top=1.1)
    plt.title('UVA-PreCOVID',fontsize=14)
    #plt.legend(loc=1,fontsize=14)

    plt.subplot(2,3,3)

    with open('Data/PreCOVID-Isolation/PreCOVID-Isolation-0.pkl', 'rb') as pkl:       
        cum_new_cases_no, cum_new_cases_rand, cum_new_cases_deg, cum_new_cases_greedy, cum_new_cases_shorr, loads_other_no, loads_other_rand, loads_other_deg, loads_other_greedy, loads_other_shorr, rhos_rand, rhos_deg, rhos_greedy, rhos_shorr = pickle.load(pkl)

    Start = 20
    End = 100

    ThresholdList = range(Start,End+1,1)

    XValue = []
    XLabel = []
    for X in range(Start,End+1,10):
        XValue.append((X-Start))
        XLabel.append(str(X))

    for k in [4000]:

        Rand = []
        Deg = []
        Shorr = []
        Greedy = []

        with open('Data/PreCOVID-Isolation/PreCOVID-Isolation-0.pkl', 'rb') as pkl:       
            cum_new_cases_no, cum_new_cases_rand, cum_new_cases_deg, cum_new_cases_greedy, cum_new_cases_shorr, loads_other_no, loads_other_rand, loads_other_deg, loads_other_greedy, loads_other_shorr, rhos_rand, rhos_deg, rhos_greedy, rhos_shorr = pickle.load(pkl)

        for threshold in ThresholdList:
            Rand.append(len(np.where(cum_new_cases_rand[int((k-500)/500),:,-1]>threshold)[0]))
            Deg.append(len(np.where(cum_new_cases_deg[int((k-500)/500),:,-1]>threshold)[0]))
            Shorr.append(len(np.where(cum_new_cases_shorr[int((k-500)/500),:,-1]>threshold)[0]))
            Greedy.append(len(np.where(cum_new_cases_greedy[int((k-500)/500),:,-1]>threshold)[0]))
            
        X = np.array(list(range(len(ThresholdList)))) + 1

        plt.plot(X, Rand, '-', label='Random', linewidth=2, color='C7')
        plt.plot(X, Deg, '-', label='Degree', linewidth=2, color='C0')
        plt.plot(X, Shorr, '-', label='Shorr Score', linewidth=2, color='#6B8E23')
        plt.plot(X, Greedy, '-', label='Greedy-Spectral', linewidth=2, color='C3')

        plt.xlabel("Target", fontsize=18)
        plt.ylabel(r"$Prob[Cases > Target]$", fontsize=18)
        plt.xticks(XValue,XLabel,fontsize=12)
        plt.xlim(0,80)
        plt.yticks([0,200,400,600,800,1000],['0','0.2','0.4','0.6','0.8','1.0'],fontsize=12)
        plt.ylim(bottom=0,top=1000)
        
        plt.title('UVA-PreCOVID: Budget k='+str(k),fontsize=14)

    plt.subplot(2,3,4)

    with open('Data/PostCOVID-Isolation/PostCOVID-Isolation-0.pkl', 'rb') as pkl:       
        cum_new_cases_no, cum_new_cases_rand, cum_new_cases_deg, cum_new_cases_greedy, cum_new_cases_shorr, loads_other_no, loads_other_rand, loads_other_deg, loads_other_greedy, loads_other_shorr, rhos_rand, rhos_deg, rhos_greedy, rhos_shorr = pickle.load(pkl)

    NoMean = []
    RandMean = []
    RandStd = []
    DegMean = []
    DegStd = []
    ShorrMean = []
    ShorrStd = []
    GreedyMean = []
    GreedyStd = []

    for k in range(500,5001,500):
        NoMean.append(np.mean(np.sum(loads_other_no[int((k-500)/500),:,:],axis=1)))
        RandMean.append(np.mean(np.sum(loads_other_rand[int((k-500)/500),:,:],axis=1)))
        RandStd.append(np.std(np.sum(loads_other_rand[int((k-500)/500),:,:],axis=1)))
        DegMean.append(np.mean(np.sum(loads_other_deg[int((k-500)/500),:,:],axis=1)))
        DegStd.append(np.std(np.sum(loads_other_deg[int((k-500)/500),:,:],axis=1)))
        ShorrMean.append(np.mean(np.sum(loads_other_shorr[int((k-500)/500),:,:],axis=1)))
        ShorrStd.append(np.std(np.sum(loads_other_shorr[int((k-500)/500),:,:],axis=1)))
        GreedyMean.append(np.mean(np.sum(loads_other_greedy[int((k-500)/500),:,:],axis=1)))
        GreedyStd.append(np.std(np.sum(loads_other_greedy[int((k-500)/500),:,:],axis=1)))

    RandMean = np.array(RandMean)/np.array(NoMean)
    RandStd = np.array(RandStd)/np.array(NoMean)
    DegMean = np.array(DegMean)/np.array(NoMean)
    DegStd = np.array(DegStd)/np.array(NoMean)
    ShorrMean = np.array(ShorrMean)/np.array(NoMean)
    ShorrStd = np.array(ShorrStd)/np.array(NoMean)
    GreedyMean = np.array(GreedyMean)/np.array(NoMean)
    GreedyStd = np.array(GreedyStd)/np.array(NoMean)

    x1 = np.array(list(range(10))) + 1 - 0.3
    x2 = np.array(list(range(10))) + 1 - 0.1
    x3 = np.array(list(range(10))) + 1 + 0.1
    x4 = np.array(list(range(10))) + 1 + 0.3

    plt.bar(x1,RandMean,yerr=RandStd,capsize=4,color='C7',label='Random',width=0.2)
    plt.bar(x2,DegMean,yerr=DegStd,capsize=4,color='C0',label='Degree',width=0.2)
    plt.bar(x3,ShorrMean,yerr=ShorrStd,capsize=4,color='#6B8E23',label='Shorr',width=0.2)
    plt.bar(x4,GreedyMean,yerr=GreedyStd,capsize=4, color='C3',label='Greedy-Spectral',width=0.2)

    plt.xlabel(r"Budget $k$"+"\n\n(a) "+r"$\gamma_{Loads}$", fontsize=18)
    plt.ylabel(r"$\gamma_{Loads}$", fontsize=18)
    plt.hlines(1,0.5,10.5,linewidth=1,color='black',linestyle='dashed')
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10],[0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000],fontsize=10)
    plt.yticks([0,0.2,0.4,0.6,0.8,1.0],[0,0.2,0.4,0.6,0.8,1.0],fontsize=12)
    plt.xlim(0.5,10.5)
    plt.ylim(bottom=0,top=1.1)
    plt.title('UVA-PostCOVID',fontsize=14)
    plt.legend(loc=1,fontsize=14)

    plt.subplot(2,3,5)

    with open('Data/PostCOVID-Isolation/PostCOVID-Isolation-0.pkl', 'rb') as pkl:       
        cum_new_cases_no, cum_new_cases_rand, cum_new_cases_deg, cum_new_cases_greedy, cum_new_cases_shorr, loads_other_no, loads_other_rand, loads_other_deg, loads_other_greedy, loads_other_shorr, rhos_rand, rhos_deg, rhos_greedy, rhos_shorr = pickle.load(pkl)

    NoMean = []
    RandMean = []
    RandStd = []
    DegMean = []
    DegStd = []
    ShorrMean = []
    ShorrStd = []
    GreedyMean = []
    GreedyStd = []

    for k in range(500,5001,500):
        NoMean.append(np.mean(cum_new_cases_no[int((k-500)/500),:,-1]))
        RandMean.append(np.mean(cum_new_cases_rand[int((k-500)/500),:,-1]))
        RandStd.append(np.std(cum_new_cases_rand[int((k-500)/500),:,-1]))
        DegMean.append(np.mean(cum_new_cases_deg[int((k-500)/500),:,-1]))
        DegStd.append(np.std(cum_new_cases_deg[int((k-500)/500),:,-1]))
        ShorrMean.append(np.mean(cum_new_cases_shorr[int((k-500)/500),:,-1]))
        ShorrStd.append(np.std(cum_new_cases_shorr[int((k-500)/500),:,-1]))
        GreedyMean.append(np.mean(cum_new_cases_greedy[int((k-500)/500),:,-1]))
        GreedyStd.append(np.std(cum_new_cases_greedy[int((k-500)/500),:,-1]))

    RandMean = np.array(RandMean)/np.array(NoMean)
    RandStd = np.array(RandStd)/np.array(NoMean)
    DegMean = np.array(DegMean)/np.array(NoMean)
    DegStd = np.array(DegStd)/np.array(NoMean)
    ShorrMean = np.array(ShorrMean)/np.array(NoMean)
    ShorrStd = np.array(ShorrStd)/np.array(NoMean)
    GreedyMean = np.array(GreedyMean)/np.array(NoMean)
    GreedyStd = np.array(GreedyStd)/np.array(NoMean)

    x1 = np.array(list(range(10))) + 1 - 0.3
    x2 = np.array(list(range(10))) + 1 - 0.1
    x3 = np.array(list(range(10))) + 1 + 0.1
    x4 = np.array(list(range(10))) + 1 + 0.3

    plt.bar(x1,RandMean,yerr=RandStd,capsize=4,color='C7',label='Random',width=0.2)
    plt.bar(x2,DegMean,yerr=DegStd,capsize=4,color='C0',label='Degree',width=0.2)
    plt.bar(x3,ShorrMean,yerr=ShorrStd,capsize=4,color='#6B8E23',label='Shorr',width=0.2)
    plt.bar(x4,GreedyMean,yerr=GreedyStd,capsize=4, color='C3',label='Greedy-Spectral',width=0.2)

    plt.xlabel(r"Budget $k$"+"\n\n(b) "+r"$\gamma_{Cases}$", fontsize=18)
    plt.ylabel(r"$\gamma_{Cases}$", fontsize=18)
    plt.hlines(1,0.5,10.5,linewidth=1,color='black',linestyle='dashed')
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10],[0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000],fontsize=10)
    plt.yticks([0,0.2,0.4,0.6,0.8,1.0],[0,0.2,0.4,0.6,0.8,1.0],fontsize=12)
    plt.xlim(0.5,10.5)
    plt.ylim(bottom=0,top=1.1)
    plt.title('UVA-PostCOVID',fontsize=14)
    #plt.legend(loc=1,fontsize=14)

    plt.subplot(2,3,6)

    with open('Data/PostCOVID-Isolation/PostCOVID-Isolation-0.pkl', 'rb') as pkl:       
        cum_new_cases_no, cum_new_cases_rand, cum_new_cases_deg, cum_new_cases_greedy, cum_new_cases_shorr, loads_other_no, loads_other_rand, loads_other_deg, loads_other_greedy, loads_other_shorr, rhos_rand, rhos_deg, rhos_greedy, rhos_shorr = pickle.load(pkl)

    Start = 20
    End = 100

    ThresholdList = range(Start,End+1,1)

    XValue = []
    XLabel = []
    for X in range(Start,End+1,10):
        XValue.append((X-Start))
        XLabel.append(str(X))

    for k in [4000]:

        Rand = []
        Deg = []
        Shorr = []
        Greedy = []

        with open('Data/PostCOVID-Isolation/PostCOVID-Isolation-0.pkl', 'rb') as pkl:       
            cum_new_cases_no, cum_new_cases_rand, cum_new_cases_deg, cum_new_cases_greedy, cum_new_cases_shorr, loads_other_no, loads_other_rand, loads_other_deg, loads_other_greedy, loads_other_shorr, rhos_rand, rhos_deg, rhos_greedy, rhos_shorr = pickle.load(pkl)

        for threshold in ThresholdList:
            Rand.append(len(np.where(cum_new_cases_rand[int((k-500)/500),:,-1]>threshold)[0]))
            Deg.append(len(np.where(cum_new_cases_deg[int((k-500)/500),:,-1]>threshold)[0]))
            Shorr.append(len(np.where(cum_new_cases_shorr[int((k-500)/500),:,-1]>threshold)[0]))
            Greedy.append(len(np.where(cum_new_cases_greedy[int((k-500)/500),:,-1]>threshold)[0]))
            
        X = np.array(list(range(len(ThresholdList)))) + 1

        plt.plot(X, Rand, '-', label='Random', linewidth=2, color='C7')
        plt.plot(X, Deg, '-', label='Degree', linewidth=2, color='C0')
        plt.plot(X, Shorr, '-', label='Shorr Score', linewidth=2, color='#6B8E23')
        plt.plot(X, Greedy, '-', label='Greedy-Spectral', linewidth=2, color='C3')

        plt.xlabel("Target\n\n(c) "+r"$Prob[Cases > Target]$", fontsize=18)
        plt.ylabel(r"$Prob[Cases > Target]$", fontsize=18)
        plt.xticks(XValue,XLabel,fontsize=12)
        plt.xlim(0,80)
        plt.yticks([0,200,400,600,800,1000],['0','0.2','0.4','0.6','0.8','1.0'],fontsize=12)
        plt.ylim(bottom=0,top=1000)
        
        plt.title('UVA-PostCOVID: Budget k='+str(k),fontsize=14)
        
    plt.tight_layout()
    plt.savefig('Figure5.pdf')

    
    
