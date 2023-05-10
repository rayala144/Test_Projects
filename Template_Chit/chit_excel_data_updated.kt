import org.apache.poi.ss.usermodel.Font
import org.apache.poi.xssf.usermodel.XSSFRow
import org.apache.poi.xssf.usermodel.XSSFWorkbook
import java.io.File
import java.util.regex.Pattern

fun main() {
    val workbook = XSSFWorkbook(File("Template_Chit/chit_data_1.xlsx"))

    fun createSheet(sheetNum: Int) = workbook.getSheetAt(sheetNum - 1)

    fun getNumData(startRow: Int, column: String, sheet: org.apache.poi.ss.usermodel.Sheet): Map<String, Double> {
        val dataNum = mutableMapOf<String, Double>()
        var endRow = startRow
        var itrCell = sheet.getRow(startRow - 1).getCell(column)
        while (itrCell.stringCellValue.isNotBlank()) {
            dataNum[(endRow - startRow + 1).toString()] = itrCell.numericCellValue
            endRow += 1
            itrCell = sheet.getRow(endRow - 1).getCell(column)
        }
        return dataNum
    }

    val data2 = getNumData(3, "B", createSheet(1))
    val numList = (1..data2.size).map { it.toString() }
    val totals = mutableListOf<Double>()

    fun autoFillSum(startRow: Int, endRow: Int, column: String, sheet: org.apache.poi.ss.usermodel.Sheet) {
        var totalSum = 0.0
        for (row in startRow..endRow) {
            val cell = sheet.getRow(row - 1).getCell(column)
            val value = cell.stringCellValue
            if (value.isNotBlank()) {
                val strList = Pattern.compile("\\d+").matcher(value).results().map { it.group() }
                var tempSum = 0.0
                var count = 0
                for (digit in strList) {
                    if (digit in numList) {
                        count += 1
                        tempSum += data2[digit]
                    } else {
                        tempSum = 0.0
                        break
                    }
                }
                totalSum += tempSum
                val nextCell = sheet.getRow(row - 1).getCell((column[0].toInt() + 1).toChar().toString())
                nextCell.setCellValue(tempSum)
            }
        }
        val sumCell = sheet.getRow(endRow).getCell((column[0].toInt() + 1).toChar().toString())
        sumCell.setCellValue(totalSum)
        sumCell.cellStyle = workbook.createCellStyle().apply { setFont(Font().apply { setBold(true) }) }
        totals.add(totalSum)
    }

    autoFillSum(3, 32, "B", createSheet(2))
    autoFillSum(3, 32, "E", createSheet(2))
    autoFillSum(3, 40, "B", createSheet(3))
    autoFillSum(3, 40, "E", createSheet(3))

    // Grand total
    createSheet(3).createRow(42).createCell(4).setCellValue("GRAND TOTAL")
    createSheet(3).createRow(42).createCell(5).setCellValue(totals.sum())
    createSheet(3).getRow(42).getCell(4).cellStyle = workbook.createCellStyle().apply {
        setFont(Font().apply { setBold(true); setItalic(true); setFontHeightInPoints(14.toShort()) })
    }

    // save file
    workbook.write(File("Template_Chit/chit_data_3.xlsx"))
    workbook.close()
}
