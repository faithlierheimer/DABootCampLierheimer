Attribute VB_Name = "Module1"
Sub minmax()

'Declare needed variables
    Dim rng As Range
    Dim rng2 As Range
    Dim dblMax As Double
    Dim rowMax As Long
    Dim dblMin As Double
    Dim rowMin As Long
    Dim gvolume As Double
    Dim rowVol As Long
 'Define range to search for max/min percent change
    Set rng = ActiveSheet.Range("L:L")
    
'Find max/min percent change
    dblMax = Application.WorksheetFunction.Max(rng)
    dblMin = Application.WorksheetFunction.Min(rng)

'Find row reference that corresponds to the max and min percent change
    rowMax = Application.Match(dblMax, rng, 0)
    rowMin = Application.Match(dblMin, rng, 0)

'Print out ticker values that correspond with min and max percent change
    Cells(2, 15).Value = Cells(rowMax, 10).Value
    Cells(2, 16).Value = dblMax
    Cells(2, 16).NumberFormat = "0.00%"
    Cells(3, 15).Value = Cells(rowMin, 10).Value
    Cells(3, 16).Value = dblMin
    Cells(3, 16).NumberFormat = "0.00%"
    
'Define range to search for greatest total stock volume
    Set rng2 = ActiveSheet.Range("M:M")

'Find greatest total stock volume
 gvolume = Application.WorksheetFunction.Max(rng2)
 
 'Find row reference that corresponds to the greatest total stock volume
 rowVol = Application.Match(gvolume, rng2, 0)
 
 'Print out ticker value that corresponds with greatest total stock volume
 Cells(4, 15).Value = Cells(rowVol, 10).Value
 Cells(4, 16).Value = gvolume
 Cells(4, 16).NumberFormat = "000,000"
 
 'Label each row appropriately for challenge summary table
 Cells(2, 14).Value = "Greatest % Increase"
 Range("N:N").Columns.AutoFit
 Cells(3, 14).Value = "Least % Increase"
 Cells(4, 14).Value = "Greatest total volume"
End Sub

