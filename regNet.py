import random

def Count0(lst):
    """Counter for couting 0 in a list"""
    counter = 0 
    for i in range(len(lst)):
        if lst[i] == 0:
            counter += 1
    return counter

def Count1(lst):
    """Counter for counting 1 in a list"""
    counter = 0
    for i in range(len(lst)):
        if lst[i] == 1:
            counter += 1
    return counter

def IndProb(gene1, gene2, lst1, lst2):
    """Generates probability of gene2 given probability of gene1"""
    prob1 = 0
    prob2 = 0
    if gene1 == 0:
        prob1 = Count0(lst1)/ len(lst1)
    if gene1 == 1:
        prob1 = Count1(lst1)/ len(lst1)
    if gene2 == 0:
        prob2 = Count0(lst2)/ len(lst2)
    if gene2 == 1:
        prob2 = Count1(lst2)/ len(lst2)
    return prob1 * prob2

def findnodes(network):
    nodelst = []
    lst0 = []
    lst1 = []
    lst2 = []
    lst3 = []
    for i in range(len(network)):
        if 0 in network[i]:
            lst0.append(network[i][0])
        if 1 in network[i]:
            lst1.append(network[i][0])
        if 2 in network[i]:
            lst2.append(network[i][0])
        if 3 in network[i]:
            lst3.append(network[i][0])
    lst0.remove(0)
    lst1.remove(1)
    lst2.remove(2)
    lst3.remove(3)
    nodelst.append(lst0)
    nodelst.append(lst1)  
    nodelst.append(lst2)
    nodelst.append(lst3)
    network = nodelst
    return network


def likelihood(exprData, network):
    '''main function for caluclating likelihood'''
    for genelst in range(len(exprData)):
        num_influencing_genes = 0
        influencing_genes = []
        for lst in network:
            if genelst in lst:
                num_influencing_genes += 1
                influencing_genes.append([network[genelst][0]])
        num_influencing_genes -= 1
        influencing_genes.remove(genelst)
    
    
