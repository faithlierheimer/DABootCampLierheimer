Attribute VB_Name = "Module3"
Sub stocksummary()
'Start with declaring needed variables
'lRow = define last row of range dynamically so it can apply to any dataset
'currentTicker = keeping track of which ticker label we are on so stock summary data
'can be stored by the appropriate ticker label
'tickerVolume to keep track of total stock volume
'start and endValue to track yearly and percent change

Dim lRow As Long
Dim currentTicker As String
Dim reportingRowIndex As Long
Dim tickerVolume As Double
Dim startValue As Double
Dim endValue As Double
Dim diff As Long
Dim percentChange As Double

'Define initial variables after declaring them
lRow = Cells(Rows.Count, 1).End(xlUp).Row
tickerVolume = 0
reportingRowIndex = 2

'Label the headers of each cell where I want the summary results to go
Cells(1, 10).Value = "Ticker Value"
Cells(1, 11).Value = "Yearly Change"
Cells(1, 12).Value = "Percent Change"
Cells(1, 13).Value = "Total Stock Volume"

'Begin for loop to analyze summary data, start in row 2 to last row
For i = 2 To lRow
    'Accumulate volume to get total volume for each ticker
    currentVolume = currentVolume + Cells(i, 7).Value
    'Initialize the value of the currentTicker variable to the first
    'available ticker
    If i = 2 Then
        currentTicker = Cells(i, 1).Value
    End If
    'As loop progresses, if the previous cell in column 1 (where the
    'ticker values are stored) is not equal to the value at which I
    'initialized the current ticker value, then that is the starting value
    '(beginning of year value) for the next stock ticker.
    'This works because while not every stock has data for every single day,
    'the data is organized at the daily level and in chronological order.
    If Cells(i - 1, 1).Value <> currentTicker Then
        startValue = Cells(i, 3).Value
    End If
    
    'As loop progresses, if the next cell in column 1 (where ticker values
    'are stored) is not equal to the value of the current ticker, then that is
    'the ending value (end of year value) for that ticker.
    
    If Cells(i + 1, 1).Value <> currentTicker Then
        endValue = Cells(i, 6).Value
        
        'Now that we have the end value for the current ticker, we need to report
        'out the actual summary data to the appropriate columns.
        
        'Put ticker label in appropriate column
        Cells(reportingRowIndex, 10).Value = currentTicker
       
        'endValue - startValue = yearly change
        Cells(reportingRowIndex, 11).Value = endValue - startValue
            'Color conditional formatting for yearly change--green for positive, red for negative
                If Cells(reportingRowIndex, 11).Value < 0 Then
                    Cells(reportingRowIndex, 11).Interior.Color = vbRed
                ElseIf Cells(reportingRowIndex, 11).Value > 0 Then
                    Cells(reportingRowIndex, 11).Interior.Color = vbGreen
                End If
                
        'Calculate percent change for currentTicker
        percentChange = (endValue - startValue) / startValue
        Cells(reportingRowIndex, 12).Value = percentChange
        Cells(reportingRowIndex, 12).NumberFormat = "0.00%"
        
        'Max/min percent change??
        Dim max_min_rng As Range
        Dim max As Double
        Dim min As Double
        Set max_min_rng = ActiveSheet.Range("L:L")
        max = Application.WorksheetFunction.max(max_min_rng)
        Cells(2, 14).NumberFormat = "0.00%"
        Cells(2, 14).Value = max
        
        'Report out total stock volume for currentTicker & format appropriately
        Cells(reportingRowIndex, 13).Value = currentVolume
        Cells(reportingRowIndex, 13).NumberFormat = "000,000"
        
      
        'Move the reportingRowIndex down one row for the next ticker
        reportingRowIndex = reportingRowIndex + 1
        
        'Change the value of the currentTicker to the next one down
        currentTicker = Cells(i + 1, 1).Value
        
        'Reset current volume so it's ready for the next iteration of the loop
        currentVolume = 0
    End If
'start loop over so it does the next ticker value.
Next i




End Sub

