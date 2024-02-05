import java.util.Arrays;
import java.util.Random;

public class School_Excercice_Objective_language_Learning {
    public static void main(String[] args) {


        System.out.println("Test obszernego zadania dodatkowego czas zacząć!\n");
        System.out.println("Test klasy nr 1 - Dron");
        System.out.println("Tworzymy 2 drony.");
        Zad_Dfeo_1.Drone drone1 = new Zad_Dfeo_1.Drone("Orion", 500, 600, 2430);
        Zad_Dfeo_1.Drone drone2 = new Zad_Dfeo_1.Drone("Andromeda", 350, 700, 1570);
        System.out.println("Każdy ma unikalne id.");
        System.out.println("Id drona numer 2:");
        drone2.showId();
        System.out.println("Id drona numer 1:");
        drone1.showId();
        System.out.println("Przentacja działania funkcji:");
        System.out.println(drone2.checkFlyParameters());
        drone2.fly(200);
        drone2.revEngine();
        System.out.println(drone2);

        System.out.println("\nTest klasy nr 2 - RacingDrone");
        System.out.println("Tworzymy 4 drony.");
        Zad_Dfeo_1.RacingDrone racingDrone1 = new Zad_Dfeo_1.RacingDrone("Lacerta", 700, 900, 220, "Zieloni", 4);
        Zad_Dfeo_1.RacingDrone racingDrone2 = new Zad_Dfeo_1.RacingDrone("Volans", 5050, 6000, 7430, "Czerwoni", 2);
        Zad_Dfeo_1.RacingDrone racingDrone3 = new Zad_Dfeo_1.RacingDrone("Cetus", 509, 630, 27, "Zieloni", 3);
        Zad_Dfeo_1.RacingDrone racingDrone4 = new Zad_Dfeo_1.RacingDrone("Copricorn", 800, 400, 930, "Czerwoni", 1);
        System.out.println("Przentacja działania funkcji:");
        Zad_Dfeo_1.RacingDrone[] racers = {racingDrone1, racingDrone2, racingDrone3, racingDrone4};
        System.out.println("Najszybszy dron to: " + Zad_Dfeo_1.RacingDrone.race(racers));
        racingDrone2.revEngine();
        System.out.println(Arrays.toString(Zad_Dfeo_1.RacingDrone.sortByPosition(racers)));
        System.out.println(racingDrone2);

        System.out.println("\nTest klasy nr 3 - RacingDrone");
        System.out.println("Tworzymy 2 drony.");
        Zad_Dfeo_1.VampireDrone vampireDrone1 = new Zad_Dfeo_1.VampireDrone("Sirius", 7000, 9000, 2720, false);
        Zad_Dfeo_1.VampireDrone vampireDrone2 = new Zad_Dfeo_1.VampireDrone("Vega", 50, 900, 730, true);
        System.out.println("Przentacja działania funkcji:");
        vampireDrone1.drainEnergy(racingDrone2);
        vampireDrone1.TurnIntoBatDrone();
        vampireDrone1.TurnIntoBatDrone();
        vampireDrone1.drainEnergy(racingDrone2);
        vampireDrone2.TurnIntoDrone();
        vampireDrone2.TurnIntoDrone();
        System.out.println(vampireDrone1);

        System.out.println("\nTest klasy nr 4 i 5 - ChristmasDrone i Gift");
        System.out.println("Tworzymy drona.");
        Zad_Dfeo_1.Gift gift1 = new Zad_Dfeo_1.Gift("Piłka", 0.20);
        Zad_Dfeo_1.ChristmasDrone christmasDrone1 = new Zad_Dfeo_1.ChristmasDrone("Baltasar", 700, 2000, 820, gift1);
        System.out.println("Przentacja działania funkcji:");
        gift1.prepere();
        gift1.unpack();
        System.out.println(gift1);
        christmasDrone1.deliverGift();
        System.out.println(christmasDrone1);

        System.out.println("\nTest klasy nr 6 - DroneControleRoom");
        System.out.println("Tworzymy obiekt.");
        Zad_Dfeo_1.DroneControlRoom droneControlRoom1 = new Zad_Dfeo_1.DroneControlRoom();
        System.out.println("Przentacja działania funkcji:");
        droneControlRoom1.addNewDrone(drone1);
        droneControlRoom1.addNewDrone(drone2);
        droneControlRoom1.addNewDrone(vampireDrone2);
        droneControlRoom1.addNewDrone(christmasDrone1);
        droneControlRoom1.addNewDrone(racingDrone3);
        droneControlRoom1.addNewDrone(racingDrone2);
        droneControlRoom1.chargeAllDrones();
        System.out.println("Tyle dronów może latać: " + droneControlRoom1.countDronesThatCanFly());
        droneControlRoom1.sortAllDrones();
        System.out.println("Najsilniejszy silnik ma dron: " + droneControlRoom1.findMostPowerful());

        System.out.println("\nTest klasy nr 7 (autorskiej) - KillerDrone");
        System.out.println("Tworzymy obiekt.");
        Zad_Dfeo_1.KillerDrone killerDrone1 = new Zad_Dfeo_1.KillerDrone("Iscariota", 900, 2000, 520, "Sierp");
        System.out.println("Przentacja działania funkcji:");
        killerDrone1.kill(drone1);
        killerDrone1.kill(racingDrone4);
        killerDrone1.checkWantedPoster();
        System.out.println(killerDrone1.playWithPolice(1) + " to liczba policjantów, którzy w dzisiejszym dniu brali udział w pościgu.");
        System.out.println(killerDrone1);

        System.out.println("\n\nDziękuję za uwagę!");

    }


    public static class Drone{
        int uniqueId;
        static int Id;
        String name;
        double weight;
        // Podana w g
        double enginePower;
        // Podana w W
        double batteryLevel;
        // Podana w mAh

        Drone(String name, double weight, double enginePower, double batteryLevel) {
            this.name = name;
            this.weight = weight;
            this.enginePower = enginePower;
            this.batteryLevel = batteryLevel;
            Id++;
            uniqueId = Id;

        }

        void showId() {
            System.out.println(this.uniqueId);
        }



        public boolean checkFlyParameters() {
            return this.enginePower > this.weight && this.batteryLevel > 0;
        }

        public void fly(double distance /* Podany w metrach */) {
            if (this.batteryLevel >= distance / 10 /* Zakładamy, że 1 mAh wystarcza na 10 metrów lotu */ ) {
                System.out.println("Let's fly!");
            } else {
                System.out.println("Battery level too low!");
            }
        }

        public void revEngine() {
            for (int i = 0; i < (int) (this.enginePower / this.weight); i++) {
                System.out.println("Vroom");
            }
        }

        @Override
        public String toString() {
            return "RacingDrone{" +
                    "name='" + name + '\'' +
                    ", weight=" + weight +
                    ", enginePower=" + enginePower +
                    ", batteryLevel=" + batteryLevel + '\'' +
                    '}';
        }
    }

    public static class RacingDrone extends Zad_Dfeo_1.Drone {

        String racingTeam;
        int positionInRanking;
        RacingDrone(String name, double weight, double enginePower, double batteryLevel, String racingTeam, int positionInRanking) {
            super(name, weight, enginePower, batteryLevel);
            this.positionInRanking = positionInRanking;
            this.racingTeam = racingTeam;
        }

        public static Zad_Dfeo_1.Drone race(Zad_Dfeo_1.Drone[] racers) {
            Zad_Dfeo_1.Drone fastestDrone = racers[0];
            for (int i = 1; i < racers.length; i++) {
                if (racers[i].enginePower > fastestDrone.enginePower) {
                    fastestDrone = racers[i];
                }
            }
            return fastestDrone;
        }

        public void revEngine() {
            super.revEngine();
            System.out.println("ZOOOOOM");
        }

        public static Zad_Dfeo_1.RacingDrone[] sortByPosition(Zad_Dfeo_1.RacingDrone[] racers) {
            for (int j = 0; j < racers.length; j++){
                for (int i = 0; i < racers.length - 1; i++)
                    if (racers[i].positionInRanking > racers[i + 1].positionInRanking) {
                        Zad_Dfeo_1.RacingDrone temp = racers[i];
                        racers[i] = racers[i + 1];
                        racers[i + 1] = temp;
                    } else if (racers[i].positionInRanking == racers[i + 1].positionInRanking) {
                        if (racers[i].enginePower > racers[i + 1].enginePower) {
                            Zad_Dfeo_1.RacingDrone temp = racers[i];
                            racers[i] = racers[i + 1];
                            racers[i + 1] = temp;
                        }


                    }
            }
            return racers;
        }

        @Override
        public String toString() {
            return "RacingDrone{" +
                    "name='" + name + '\'' +
                    ", weight=" + weight +
                    ", enginePower=" + enginePower +
                    ", batteryLevel=" + batteryLevel + '\'' +
                    ", racingTeam='" + racingTeam +
                    ", positionInRanking='" + positionInRanking +
                    '}';
        }

    }

    public static class VampireDrone extends Zad_Dfeo_1.Drone {
        static String constructor = "Bram Stoker";
        boolean isTransformed = false;
        // W zadaniu jest isDoneBat, ale później występuje jako isTransformed, więc zostawiam tę opcję
        // Mam nadzieję, że rozumiem ten zamysł poprawnie i niczego nie pomijam

        VampireDrone(String name, double weight, double enginePower, double batteryLevel, boolean isTransformed) {
            super(name, weight, enginePower, batteryLevel);
            this.isTransformed = isTransformed;
        }

        public void drainEnergy(Zad_Dfeo_1.Drone drone) {
            // Z tego co rozumiem z zadania, to jeśli isTransformed jest false, to dron otrzymuje funkcje wampiryczne, ale zostawiłęm to u mnie, że jeśli jest true to ma te funkcjie dla jaśniejszej czytelności z mojej strony przy pisaniu
            if (this.isTransformed) {
                this.batteryLevel = this.batteryLevel + (drone.batteryLevel / 2);
                drone.batteryLevel = drone.batteryLevel / 2;
            } else {
                System.out.println("W formie drona nie można wysysać energii.");
            }
        }

        public void TurnIntoBatDrone() {
            if (!this.isTransformed) {
                System.out.println("Od teraz to ja jestem władcą nocy!");
                this.isTransformed = true;
                this.weight = this.weight / 2;
                this.batteryLevel = this.batteryLevel / 2;
            } else {
                System.out.println("Już jestem władcą nocy.");
            }
        }

        public  void TurnIntoDrone() {
            // Dodałem od siebie funkcję powrotu do normalnego stanu
            if (this.isTransformed) {
                System.out.println("Powrót do formy słabeusza!");
                this.weight = this.weight * 2;
                this.batteryLevel = this.batteryLevel * 1.5;
                this.isTransformed = false;
            } else {
                System.out.println("Już jestem słaby, bardziej nie mogę.");
            }
        }

        @Override
        public String toString() {
            return "VampireDrone{" +
                    "name='" + name + '\'' +
                    ", weight=" + weight +
                    ", enginePower=" + enginePower +
                    ", batteryLevel=" + batteryLevel + '\'' +
                    ", isTransformed='" + isTransformed +
                    '}';
        }
    }

    public static class ChristmasDrone extends Zad_Dfeo_1.Drone {
        Zad_Dfeo_1.Gift gift;

        ChristmasDrone(String name, double weight, double enginePower, double batteryLevel, Zad_Dfeo_1.Gift gift) {
            super(name, weight, enginePower, batteryLevel);
            this.gift = gift;
        }

        public void deliverGift() {
            if (this.gift.weight + this.weight > this.enginePower) {
                System.out.println("Paczka jest zbyt ciężka żeby ją dostarczyć.");
            } else if (this.gift == null) {
                System.out.println("Nie ma żadnej paczki do dostarczenia.");
            } else {
                System.out.println("Dostarczono paczkę o wadze " + this.gift.weight + "g.");
                this.gift = null;
            }
        }

        @Override
        public String toString() {
            return "ChristmasDrone{" +
                    "name='" + name + '\'' +
                    ", weight=" + weight +
                    ", enginePower=" + enginePower +
                    ", batteryLevel=" + batteryLevel + '\'' +
                    ", gift='" + gift +
                    '}';
        }
    }

    public static class Gift {
        String nameOfContent;
        double weight;
        boolean isReadyToBeDelivered = false;

        Gift(String nameOfContent, double weight) {
            this.nameOfContent = nameOfContent;
            this.weight = weight;
        }

        public void prepere() {
            this.isReadyToBeDelivered = true;
        }

        public void unpack() {
            this.isReadyToBeDelivered = false;
            System.out.println("W paczce znajduje się " + this.nameOfContent + "!");
        }

        @Override
        public String toString() {
            return "Gift{" +
                    "nameOfContent='" + nameOfContent + '\'' +
                    ", weight=" + weight +
                    '}';
        }
    }

    public static class DroneControlRoom{
        Zad_Dfeo_1.Drone[] allDrones;
        static double windPowerOutside = 3;

        DroneControlRoom() {
            this.allDrones = new Zad_Dfeo_1.Drone[1];
        }

        public int countDronesThatCanFly() {
            getOutNulls();
            int count = 0;
            for (Zad_Dfeo_1.Drone drone: this.allDrones) {
                if (drone.enginePower > drone.weight && drone.batteryLevel > 0) {
                    count++;
                }

            }
            return count;
        }

        public void chargeAllDrones() {
            getOutNulls();
            for (Zad_Dfeo_1.Drone drone: this.allDrones) {
                drone.batteryLevel += 20;
            }
        }

        public void addNewDrone(Zad_Dfeo_1.Drone drone) {
            Zad_Dfeo_1.Drone[] newAllDrones = new Zad_Dfeo_1.Drone[allDrones.length + 1];
            for (int i = 0; i < allDrones.length; i++) {
                newAllDrones[i] = allDrones[i];
            }
            allDrones = newAllDrones;
            allDrones[allDrones.length - 1] = drone;
        }

        public void sortAllDrones() {
            getOutNulls();
            for (int i = 0; i < allDrones.length; i++) {
                for (int j = 0; j < allDrones.length - 1; j++) {
                    if (allDrones[j].weight > allDrones[j + 1].weight) {
                        double temp = allDrones[j + 1].weight;
                        allDrones[j + 1].weight = allDrones[j].weight;
                        allDrones[j].weight = temp;
                    }
                }
            }

            System.out.print(" Lista dronów posortowana po wadze (rosnąco): ");
            for (Zad_Dfeo_1.Drone drone: allDrones) {
                System.out.print(drone + ", ");
            }
        }

        public void getOutNulls() {
            int counter = 0;
            for (int j = 0; j < allDrones.length; j++) {
                if (allDrones[j] != null) {
                    counter++;
                }
            }
            Zad_Dfeo_1.Drone[] newList = new Zad_Dfeo_1.Drone[counter];
            int counter2 = 0;
            for (int j = 0; j < allDrones.length; j++) {
                if (allDrones[j] != null) {
                    newList[counter2] = allDrones[j];
                    counter2++;
                }
            }
            allDrones = newList;
        }

        public Zad_Dfeo_1.Drone findMostPowerful(){
            getOutNulls();
            return findMostPowerful(0, allDrones[0]);
        }
        public Zad_Dfeo_1.Drone findMostPowerful(int currentIndex, Zad_Dfeo_1.Drone currentMostPowerful) {
            if (currentIndex == allDrones.length) {
                return currentMostPowerful;
            }

            if (allDrones[currentIndex].enginePower > currentMostPowerful.enginePower) {
                currentMostPowerful = allDrones[currentIndex];
            }

            return findMostPowerful(currentIndex + 1, currentMostPowerful);
        }

        @Override
        public String toString() {
            return "DroneControlRoom{" +
                    "allDrones='" + Arrays.toString(allDrones) +
                    '}';
        }

    }

    // Inwencja twórcza
    public static class KillerDrone extends Zad_Dfeo_1.Drone {
        int killCounter;
        String weapon;
        int reward;

        KillerDrone(String name, double weight, double enginePower, double batteryLevel, String weapon) {
            super(name, weight, enginePower, batteryLevel);
            this.weapon = weapon;
        }

        public void kill(Zad_Dfeo_1.Drone drone) {
            System.out.println(drone.name + " został zabity przy pomocy " + this.weapon + "!");
            drone = null;
            this.killCounter++;
            reward += 10000;
        }

        public void checkWantedPoster() {
            System.out.println("Obecna nagroda za głowę " + this.name + " wynosi " + this.reward + ".");
        }

        public int playWithPolice(int policeInPursuit) {
            if (policeInPursuit > 20) {
                System.out.println(this.name + " został schwytany!");
                return policeInPursuit;
            } else if (policeInPursuit > 14) {
                System.out.println(this.name + " znów zabawił się z policją i uciekł!");
                return policeInPursuit;
            } else {
                Random random = new Random();
                return playWithPolice(policeInPursuit + random.nextInt(10));
            }
        }

        @Override
        public String toString() {
            return "KillerDrone{" +
                    "name='" + name + '\'' +
                    ", weight=" + weight +
                    ", enginePower=" + enginePower +
                    ", batteryLevel=" + batteryLevel + '\'' +
                    ", weapon='" + weapon +
                    '}';
        }

    }

}
