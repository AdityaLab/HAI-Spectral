import matplotlib.pyplot as plt
import numpy as np
import pickle

if __name__ == '__main__':

    Figure = plt.figure(figsize=(10.24,4.48))

    plt.subplot(1,2,1)

    with open('Data/PreCOVID-Clearance/PreCOVID-Clearance-0.pkl', 'rb') as pkl:       
        cum_new_cases_no, cum_new_cases_rand, cum_new_cases_deg, cum_new_cases_greedy, cum_new_cases_shorr, loads_other_no, loads_other_rand, loads_other_deg, loads_other_greedy, loads_other_shorr, rhos_rand, rhos_deg, rhos_greedy, rhos_shorr = pickle.load(pkl)
    
    rho_original = 2.1205965655507413
    
    X = np.array(list(range(500,5001,500)))
    
    plt.plot(X, list(rhos_rand/rho_original)+[1], '-', label='Random', linewidth=2, color='C7', alpha=1)
    
    plt.plot(X, list(rhos_deg/rho_original)+[1], '-', label='Degree', linewidth=2, color='C0', alpha=1)

    plt.plot(X, list(rhos_shorr/rho_original)+[1], '-', label='Shorr', linewidth=2, color='#6B8E23', alpha=1)
    
    plt.plot(X, list(rhos_greedy/rho_original)+[1], '-', label='Greedy-Spectral', linewidth=2, color='C3', alpha=1)
    
    plt.xlabel(r"Budget $k$"+"\n\n(a) UVA-PreCOVID", fontsize=18)
    plt.ylabel(r"$\eta_{\rho(A)}$", fontsize=18)
    plt.xticks([500,1000,1500,2000,2500,3000,3500,4000,4500,5000],[500,1000,1500,2000,2500,3000,3500,4000,4500,5000],fontsize=10)
    plt.yticks([0,0.2,0.4,0.6,0.8,1.0],['0','0.2','0.4','0.6','0.8','1.0'],fontsize=12)
    plt.legend(loc=2,fontsize=14)

    plt.subplot(1,2,2)

    with open('Data/PostCOVID-Clearance/PostCOVID-Clearance-0.pkl', 'rb') as pkl:       
        cum_new_cases_no, cum_new_cases_rand, cum_new_cases_deg, cum_new_cases_greedy, cum_new_cases_shorr, loads_other_no, loads_other_rand, loads_other_deg, loads_other_greedy, loads_other_shorr, rhos_rand, rhos_deg, rhos_greedy, rhos_shorr = pickle.load(pkl)
    
    rho_original = 7814765560462431.0
    
    X = np.array(list(range(500,5001,500)))
    
    plt.plot(X, list(rhos_rand/rho_original)+[1], '-', label='Random', linewidth=2, color='C7', alpha=1)
    
    plt.plot(X, list(rhos_deg/rho_original)+[1], '-', label='Degree', linewidth=2, color='C0', alpha=1)

    plt.plot(X, list(rhos_shorr/rho_original)+[1], '-', label='Shorr', linewidth=2, color='#6B8E23', alpha=1)
    
    plt.plot(X, list(rhos_greedy/rho_original)+[1], '-', label='Greedy-Spectral', linewidth=2, color='C3', alpha=1)
    
    plt.xlabel(r"Budget $k$"+"\n\n(b) UVA-COVID", fontsize=18)
    plt.ylabel(r"$~$", fontsize=18)
    plt.xticks([500,1000,1500,2000,2500,3000,3500,4000,4500,5000],[500,1000,1500,2000,2500,3000,3500,4000,4500,5000],fontsize=10)
    plt.yticks([0,0.2,0.4,0.6,0.8,1.0],['0','0.2','0.4','0.6','0.8','1.0'],fontsize=12)
    #plt.legend(loc=1,fontsize=14)
    
    plt.tight_layout()
    plt.savefig('FigureS1.pdf')

    
    
