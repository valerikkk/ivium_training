# big_data['concentration']= big_data['concentration'].apply(lambda x: '{:.10f}'.format(float(x)))
# antibiotic_conversation = {'antibiotic': {'cefazoline': 0, 'ceftiofur': 1, 'milk': 2, 'penicillin': 3, 'streptomycin': 4, 'tetracycline': 5}}
# big_data_antibiotic_class = big_data.replace(antibiotic_conversation)
#
# no_problems = big_data_antibiotic_class.drop_duplicates(['antibiotic', 'concentration'])









# X_clf, y_clf =big_data_antibiotic_class.drop('antibiotic', axis=1),\
#    big_data_antibiotic_class['antibiotic']
# X_clf_train, X_clf_test, y_clf_train, y_clf_test = train_test_split(X_clf, y_clf, test_size=0.3)
#
# # X_lnr_train, X_lnr_test, y_lnr_train, y_lnr_test = train_test_split(X_lnr, y_lnr, test_size=0.3)
#
# clf = RandomForestClassifier()
# params = {'n_estimators': range(30,150,5), 'max_depth': range(5,30)}
# search = GridSearchCV(clf, params,n_jobs=1, cv =3)
# search.fit(X_clf_train, y_clf_train)
# print(search.best_params_)
# best_clf = search.best_estimator_
# predictions_clf = best_clf.predict(X_clf_test)
# print(best_clf.score(X_clf_test, y_clf_test))
#












# rgr = LinearRegression()
# rgr.fit(X_lnr_train, y_lnr_train)
# predictions_linear = rgr.predict(X_lnr_test)
#
#
# import matplotlib.pyplot as plt
#
# plt.scatter(X_lnr_test, y_lnr_test, color='blue', label='Истинные значения')
# plt.plot(X_lnr_test, predictions_linear, color='red', linewidth=2, label='Предсказанные значения')
# plt.xlabel('Potential')
# plt.ylabel('Concentration')
# plt.legend()
# plt.show()