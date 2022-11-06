import matplotlib.pyplot as plt
import numpy as np
import pickle

if __name__ == '__main__':

    

    with open('Data/PreCOVID-Isolation/baseline.pkl', 'rb') as pkl:
        cum_new_cases_no, cum_new_cases_rand, cum_new_cases_deg, cum_new_cases_greedy, cum_new_cases_shorr,cum_new_cases_Emergency,cum_new_cases_Surgery,cum_new_cases_Device,cum_new_cases_KD = pickle.load(pkl)

    RandList = [np.mean(cum_new_cases_no[0,:,-1])]
    DegList = [np.mean(cum_new_cases_no[0,:,-1])]
    ShorrList = [np.mean(cum_new_cases_no[0,:,-1])]
    GreedyList = [np.mean(cum_new_cases_no[0,:,-1])]

    EmergencyList = [np.mean(cum_new_cases_Emergency[:,-1])]
    SurgeryList = [np.mean(cum_new_cases_Surgery[:,-1])]
    DeviceList = [np.mean(cum_new_cases_Device[:,-1])]
    KDList = [np.mean(cum_new_cases_KD[:,-1])]

    for k in range(500,5001,500):

        RandList.append(np.mean(cum_new_cases_rand[int((k-500)/500),:,-1]))
        DegList.append(np.mean(cum_new_cases_deg[int((k-500)/500),:,-1]))
        ShorrList.append(np.mean(cum_new_cases_shorr[int((k-500)/500),:,-1]))
        GreedyList.append(np.mean(cum_new_cases_greedy[int((k-500)/500),:,-1]))

        EmergencyList.append(np.mean(cum_new_cases_Emergency[:,-1]))
        SurgeryList.append(np.mean(cum_new_cases_Surgery[:,-1]))
        DeviceList.append(np.mean(cum_new_cases_Device[:,-1]))
        KDList.append(np.mean(cum_new_cases_KD[:,-1]))

    Figure = plt.figure(figsize=(5.12,3.84))

    X = np.arange(11)

    plt.plot(X, RandList, '-', label='Random', linewidth=2, color='C7')
    plt.plot(X, DegList, '-', label='Degree', linewidth=2, color='C0')
    plt.plot(X, ShorrList, '-', label='Shorr', linewidth=2, color='#6B8E23')
    plt.plot(X, GreedyList, '-', label='Greedy-Spectral', linewidth=2, color='C3')

    plt.plot(X, EmergencyList, ':', label='Emergency', linewidth=2, color='C1')
    plt.scatter([3974/500],[EmergencyList[0]], s=70, color='C1')
    plt.plot(X, SurgeryList, ':', label='Surgery', linewidth=2, color='C2')
    plt.scatter([4926/500],[SurgeryList[0]], s=70, color='C2')
    plt.plot(X, DeviceList, ':', label='Invasive device', linewidth=2, color='C4')
    plt.scatter([1510/500],[DeviceList[0]], s=70, color='C4')
    plt.plot(X, KDList, ':', label='Dialysis', linewidth=2, color='C5')
    plt.scatter([270/500],[KDList[0]], s=70, color='C5')

    
    plt.xlabel(r"Budget $k$", fontsize=14)
    plt.ylabel("Number of cases", fontsize=14)
    plt.xticks(X,['0','500','1000','1500','2000','2500','3000','3500','4000','4500','5000'],fontsize=9)
    plt.yticks([0,200,400,600,800,1000,1200],[0,200,400,600,800,1000,1200],fontsize=10)
    plt.xlim(0,10)
    plt.ylim(0,1200)
    plt.title('Relaxed precaution and cleaning scenario')
    plt.legend(fontsize=9)

    plt.tight_layout()
    plt.savefig('Figure10.pdf')
    
