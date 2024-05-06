################################################
##                                            ##
##   Problem Set Week 8                       ##
##                                            ##
################################################

# Note: Enter your results as actual numbers. We check your solution by allowing some minor margin of error. (No need to round your answers!)


########### Task (2) ###########

########### Task (2.1) ###########
# ols estimate of AR(1) coef
coeff_const_AI_PA = 0.008928
coeff_rlag1_AI_PA = -0.094084
# t-stat for AR(1) coef
t_stat_const_AI_PA = 2.963093
t_stat_rlag1_AI_PA = -1.511661
# variance of r. Hint: var(y) = sum (r-mean(r)/(len(r)-1)
var_r_AI_PA = 0.0022653254847890035 
# variance of eps Hint: var(eps) = eps.T eps / (len(r)-1-1)
var_eps_AI_PA = 0.0022539217106887595
# variance of mu. Hint: var(mu) = sum(mu-mean(mu)/(len(mu)-1)
var_mu_AI_PA = 2.0277481622640707e-05

########### Task (2.2) ###########

ticker = "MUV2.DE"
t_stat_const_ticker = 0.592064
t_stat_rlag1_ticker = -2.543809
adj_rsqr_ticker = 0.021085079446328536


########### Task (3) ###########

# ols estimate of AR(1) coef
coeff_const_market = 0.004639
coeff_rlag1_market = 0.039774
# t-stat for AR(1) coef
t_stat_const_market = 1.343152
t_stat_rlag1_market = 0.634457
# adj_R^2
adj_rsqr_market = -0.0023577688842633115
# variance of r. Hint: var(y) = sum (r-mean(r)/(len(r)-1)
var_r_market = 0.0030133318157624777 
# variance of eps Hint: var(eps) = eps.T eps / (len(r)-1-1)
var_eps_market = 0.0030204365557556434
# variance of mu. Hint: var(mu) = sum(mu-mean(mu)/(len(mu)-1)
var_mu_market = 4.7867425098091005e-06
