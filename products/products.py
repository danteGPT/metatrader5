# implments volume in matplot basead in mt5 
'''
class Products:
    def __init__(self, mt5) :
        self.mt5 = mt5
        pass

    def OnCalculate(const int rates_total,
                    const int prev_calculated,
                    const datetime &time[],
                    const double &open[],
                    const double &high[],
                    const double &low[],
                    const double &close[],
                    const long &tick_volume[],
                    const long &volume[],
                    const int &spread[])
    {
    if(rates_total<2)
        return(0);
    //--- starting work
    int pos=prev_calculated-1;
    //--- correct position
    if(pos<1)
        {
        ExtVolumesBuffer[0]=0;
        pos=1;
        }
    //--- main cycle
    if(InpVolumeType==VOLUME_TICK)
        CalculateVolume(pos,rates_total,tick_volume);
    else
        CalculateVolume(pos,rates_total,volume);
    //--- OnCalculate done. Return new prev_calculated.
    return(rates_total);
    }
    //+------------------------------------------------------------------+
    //|                                                                  |
    //+------------------------------------------------------------------+
    void CalculateVolume(const int pos,const int rates_total,const long& volume[])
    {
    ExtVolumesBuffer[0]=(double)volume[0];
    ExtColorsBuffer[0]=0.0;
    //---
    for(int i=pos; i<rates_total && !IsStopped(); i++)
        {
        double curr_volume=(double)volume[i];
        double prev_volume=(double)volume[i-1];
        //--- calculate indicator
        ExtVolumesBuffer[i]=curr_volume;
        if(curr_volume>prev_volume)
            ExtColorsBuffer[i]=0.0;
        else
            ExtColorsBuffer[i]=1.0;
        }
    //---'''