import pandas as pd
import numpy as np

rmax_zonal_stats_csv = "G:\My Drive\Year 2\Thesis\Backup_Plan\weather\\virginia\\rmax\zonal_stats\zonal_stats_rmax.csv"
tmmx_zonal_stats_csv = "G:\My Drive\Year 2\Thesis\Backup_Plan\weather\\virginia\\tmmx\zonal_stats\zonal_stats_tmmx.csv"

rmax_zonal_stats_df = pd.read_csv(rmax_zonal_stats_csv)
tmmx_zonal_stats_df = pd.read_csv(tmmx_zonal_stats_csv)

if rmax_zonal_stats_df['date'].equals(tmmx_zonal_stats_df['date']) and rmax_zonal_stats_df['clim_div'].equals(tmmx_zonal_stats_df['clim_div']):
    tmmx_f = (9/5)*(tmmx_zonal_stats_df['mean_tmmx']-273.15) + 32
    tmmx_c = tmmx_zonal_stats_df['mean_tmmx']-273.15

    heat_index = 0.5 * (tmmx_f + 61.0 + ((tmmx_f-68.0)*1.2) + (rmax_zonal_stats_df['mean_rmax']*0.094))

    df = pd.DataFrame(
        {
            'date': rmax_zonal_stats_df['date'],
            'clim_div': rmax_zonal_stats_df['clim_div'],
            'tmmx_k': tmmx_zonal_stats_df['mean_tmmx'],
            'tmmx_c': tmmx_c,
            'tmmx_f': tmmx_f,
            'rmax': rmax_zonal_stats_df['mean_rmax'],
            'heat_index': heat_index
        }
    )

    # Adjustments to heat index for specific cases
    
    df.loc[df['heat_index'] >= 80, 'heat_index'] = -42.379 + 2.04901523*df['tmmx_f'] + 10.14333127*df['rmax'] - .22475541*df['tmmx_f']*df['rmax'] - .00683783*df['tmmx_f']*df['tmmx_f'] - .05481717*df['rmax']*df['rmax'] + .00122874*df['tmmx_f']*df['tmmx_f']*df['rmax'] + .00085282*df['tmmx_f']*df['rmax']*df['rmax'] - .00000199*df['tmmx_f']*df['tmmx_f']*df['rmax']*df['rmax']
    df.loc[(df['rmax'] < 13) & (df['tmmx_f'] >= 80) & (df['tmmx_f'] <= 112), 'heat_index'] = df['heat_index'] - ((13-df['rmax'])/4)*((17-abs(df['tmmx_f']-95.0)).apply(np.sqrt)/17)
    df.loc[(df['rmax'] > 85) & (df['tmmx_f'] >= 80) & (df['tmmx_f'] <= 87), 'heat_index'] = df['heat_index'] + ((df['rmax']-85)/10) * ((87-df['tmmx_f'])/5)
    
df.to_csv("G:\My Drive\Year 2\Thesis\Backup_Plan\weather\\virginia\\all_weather\\all_weather_data.csv", index=False)



