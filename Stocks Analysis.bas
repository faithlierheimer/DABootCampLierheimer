Attribute VB_Name = "Module2"
Sub stocksummary()

Dim lRow As Long
Dim currentTicker As String
Dim reportingRowIndex As Long
Dim tickerVolume As Double
Dim startValue As Long
Dim endValue As Long
Dim diff As Long

lRow = Cells(Rows.Count, 1).End(xlUp).Row
tickerVolume = 0
reportingRowIndex = 2

Cells(1, 11).Value = "Year Open"
Cells(1, 12).Value = "Year Close"
Cells(1, 13).Value = "Yearly Change"
Cells(1, 14).Value = "Total Volume"
Cells(1, 15).Value = "Percent Change"

For i = 2 To lRow
    currentVolume = currentVolume + Cells(i, 7).Value
    If i = 2 Then
        currentTicker = Cells(i, 1).Value
    End If
    
    If Cells(i - 1, 1).Value <> currentTicker Then
        startValue = Cells(i, 3).Value
    End If
    
    If Cells(i + 1, 1).Value <> currentTicker Then
        endValue = Cells(i, 6).Value
        
        Cells(reportingRowIndex, 10).Value = currentTicker
        Cells(reportingRowIndex, 11).Value = startValue
        Cells(reportingRowIndex, 12).Value = endValue
        Cells(reportingRowIndex, 13).Value = endValue - startValue
        Cells(reportingRowIndex, 14).Value = currentVolume
        Cells(reportingRowIndex, 15).Value = (endValue - startValue) / startValue
        reportingRowIndex = reportingRowIndex + 1
        currentTicker = Cells(i + 1, 1).Value
        currentVolume = 0
    End If
Next i


'lowestnumber = Application.WorksheetFunction.Min(myrange)
'highestnumber = Application.WorksheetFunction.Max(myrange)

'Get last row
'For-loop that goes through each row


'For Each mycell In myrange
'    If mycell.Value = lowestnumber Then
    'save to variable somehow
    'aggregate by column a somehow
'    End If
'Next mycell

End Sub
