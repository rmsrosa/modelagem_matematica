
# from [CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19)
download("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv", joinpath(@__DIR__, "..", "data", "time_series_covid19_deaths_global.csv"))
download("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv", joinpath(@__DIR__, "..", "data", "time_series_covid19_recovered_global.csv"))
download("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv", joinpath(@__DIR__, "..", "data", "time_series_covid19_confirmed_global.csv"))

# from [wcota/covid19br](https://github.com/wcota/covid19br)
download("https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities-time.csv.gz", joinpath(@__DIR__, "..", "data", "cases-brazil-cities-time.csv.gz"))
download("https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv", joinpath(@__DIR__, "..", "data", "cases-brazil-states.csv"))
