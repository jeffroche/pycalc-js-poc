function formatDataForGoogleChart(xData, yData, xLabel, yLabel) {
    // Formats data for a Google chart per these docs:
    // https://developers.google.com/chart/interactive/docs/gallery/linechart?csw=1#Data_Format
    var data = [[xLabel, yLabel]];
    console.log(xData,yData);
    for (var i=0; i < yData.length; ++i) {
        data[i+1] = [xData[i], yData[i]];
    }
    return data;
}