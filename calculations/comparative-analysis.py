import statistics
from scipy.stats import sem
from scipy.stats import stats

control_prop = [0.0009482983582485355, 0.0019962211141337314, 0.0008723231534534669]
cancer_prop = [0.0008927603738634797, 0.0006631525835623202, 0.0010388306022856362]

control_mean = statistics.mean(control_prop)
cancer_mean = statistics.mean(cancer_prop)

print('control mean: ' + str(control_mean))
print('cancer mean: ' + str(cancer_mean))

control_SE = sem([0.0009482983582485355, 0.0019962211141337314, 0.0008723231534534669])
print('control SE = ' + str(control_SE))

cancer_SE = sem([0.0008927603738634797, 0.0006631525835623202, 0.0010388306022856362])
print('cancer SE = ' + str(cancer_SE))

print(stats.ttest_ind(control_prop, cancer_prop))

