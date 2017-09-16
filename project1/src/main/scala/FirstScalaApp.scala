import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._

object FirstScalaApp {

   def main(args: Array[String]) {
    val sc = new SparkContext("local", "First Spark App")
    val rawdata = sc.textFile("/Users/steve/demo_data.csv")
    val data = rawdata.map(line => line.split(",")).map( t => (t(0), t(1), t(2)) )

    // 计数类, 求和类, 频数统计
    val numPurchases = data.count()
    val uniqueUsers = data.map { case (user, product, price) => user }.distinct().count()
    val totalRevenue = data.map { case (user, product, price) => price.toDouble }.filter(price => price < 2000).sum()
    // 热销的产品
    val productByPopularity = data.map { case (user, product, price) => (product, 1) }.reduceByKey( _ + _).collect.sortBy(-_._2)
    val mostPopular = productByPopularity(0)

    println("Total purchases: " + numPurchases)
    println("Unique users: " + uniqueUsers)
    println("Total revenue: " + totalRevenue)
    println("Most popular product: %s with %d purchases".format(mostPopular._1, mostPopular._2))
}
}
