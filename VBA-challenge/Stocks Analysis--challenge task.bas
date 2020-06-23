Attribute VB_Name = "Module3"
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
    dblMax = Application.WorksheetFunction.max(rng)
    dblMin = Application.WorksheetFunction.min(rng)

'Find row reference that corresponds to the max and min percent change
    rowMax = Application.Match(dblMax, rng, 0)
    rowMin = Application.Match(dblMin, rng, 0)

'Print out ticker values that correspond with min and max percent change
    Cells(2, 14).Value = Cells(rowMax, 10).Value
    Cells(2, 15).Value = dblMax
    Cells(2, 15).NumberFormat = "0.00%"
    Cells(3, 14).Value = Cells(rowMin, 10).Value
    Cells(3, 15).Value = dblMin
    Cells(3, 15).NumberFormat = "0.00%"
    
'Define range to search for greatest total stock volume
    Set rng2 = ActiveSheet.Range("M:M")

'Find greatest total stock volume
 gvolume = Application.WorksheetFunction.max(rng2)
 
 'Find row reference that corresponds to the greatest total stock volume
 rowVol = Application.Match(gvolume, rng2, 0)
 
 'Print out ticker value that corresponds with greatest total stock volume
 Cells(4, 14).Value = Cells(rowVol, 10).Value
 Cells(4, 15).Value = gvolume
 Cells(4, 15).NumberFormat = "000,000"
End Sub
