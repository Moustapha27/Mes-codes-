import scala.collection.mutable.ListBuffer
import scala.io.StdIn.readLine

// Définition de la classe Task
case class Task(
    name: String,
    description: String,
    responsiblePerson: String,
    status: String = "À faire"
)

// Définition de la classe TaskList
class TaskList {
  private var tasks: ListBuffer[Task] = ListBuffer()

  // Ajouter une tâche à la liste
  def addTask(
      name: String,
      description: String,
      responsiblePerson: String,
      status: String = "À faire"
  ): Unit = {
    tasks += Task(name, description, responsiblePerson, status)
    println("Tâche ajoutée avec succès.")
  }

  // Afficher toutes les tâches
  def displayTasks(): Unit = {
    if (tasks.isEmpty) {
      println("Aucune tâche à afficher.")
    } else {
      tasks.zipWithIndex.foreach { case (task, index) =>
        println(
          s"${index + 1}. ${task.name} - Description: ${task.description} - Responsable: ${task.responsiblePerson} - Statut: ${task.status}"
        )
      }
    }
  }

  // Marquer une tâche comme terminée
  def updateTaskStatus(index: Int, newStatus: String): Unit = {
    if (index >= 1 && index <= tasks.length) {
      val updatedTask = tasks(index - 1).copy(status = newStatus)
      tasks(index - 1) = updatedTask
      println(s"Le statut de la tâche '${updatedTask.name}' a été mis à jour.")
    } else {
      println("Numéro de tâche invalide.")
    }
  }

  // Supprimer une tâche
  def deleteTask(index: Int): Unit = {
    if (index >= 1 && index <= tasks.length) {
      tasks.remove(index - 1)
      println("Tâche supprimée avec succès.")
    } else {
      println("Numéro de tâche invalide.")
    }
  }
}

object Main {
  def main(args: Array[String]): Unit = {
    val taskList = new TaskList()

    var running = true
    while (running) {
      println("\n=== Gestionnaire de Tâches ===")
      println("1. Ajouter une tâche")
      println("2. Afficher les tâches")
      println("3. Mettre à jour le statut d'une tâche")
      println("4. Supprimer une tâche")
      println("5. Quitter")
      print("Choisissez une option : ")

      val choice = readLine()

      choice match {
        case "1" =>
          print("Entrez le nom de la tâche : ")
          val name = readLine()
          print("Entrez la description de la tâche : ")
          val description = readLine()
          print("Entrez la personne responsable de la tâche : ")
          val responsiblePerson = readLine()
          taskList.addTask(name, description, responsiblePerson)
        case "2" =>
          taskList.displayTasks()
        case "3" =>
          print("Entrez le numéro de la tâche à mettre à jour : ")
          val index = readLine().toInt
          println(
            "Choisissez un nouveau statut (À faire, En progression, Terminé) : "
          )
          val newStatus = readLine()
          taskList.updateTaskStatus(index, newStatus)
        case "4" =>
          print("Entrez le numéro de la tâche à supprimer : ")
          val index = readLine().toInt
          taskList.deleteTask(index)
        case "5" =>
          println("Au revoir !")
          running = false
        case _ =>
          println("Option invalide.")
      }
    }
  }
}
