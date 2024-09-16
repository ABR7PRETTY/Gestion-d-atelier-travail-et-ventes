<script setup>

import Dashboard from "@/components/Dashboard.vue";
</script>

<template>
        <!-- HEADER MOBILE-->
        <!-- END HEADER MOBILE-->

          <!-- MENU SIDEBAR-->
        <aside class="menu-sidebar d-none d-lg-block">
            <div style=" height: 75px; text-align: center">
                <a href="#">
                    <img  height=50px src="../assets/images/icon/images.png" alt="Cool Admin" />
                  <marquee bgcolor="black">
                    <h3 style="color: white"> Docteur  &emsp; Michelin</h3>
                  </marquee>
                </a>
            </div>
            <div class="menu-sidebar__content js-scrollbar1">
                <nav class="navbar-sidebar">
                    <ul class="list-unstyled navbar__list">
                      <li>
                            <a href="/Dashboard">
                                <i class="fas fa-chart-bar"></i>Dashboard</a>
                        </li>
                        <li>
                        <a href="/Atelier">
                          <i class="fas fa-table"></i>Atelier</a>
                      </li>
                      <li>
                      <a href="/Mois">
                        <i class="fas fa-calendar-minus-o"></i>Mensuel</a>
                      </li>
                        <li>
                            <a href="/Designation">
                                <i class="fas fa-calendar-alt"></i>Designation Journaliere</a>
                        </li>
                        <li>
                            <a href="/Vente">
                                <i class="fas fa-money-bill-alt"></i>Vente</a>
                        </li>
                      <li>
                        <a href="/Depense">
                          <i class="fas fa-money-bill-alt"></i>Depense</a>
                      </li>
                        <li>
                            <a  href="/Categorie">
                                <i class="fas fa-copy"></i>Categorie</a>
                        </li>
                        <li >
                            <a  href="/Article">
                                <i class="fas fa-tasks"></i>Article</a>
                        </li>
                        <li>
                        <a href="/Apprenti">
                          <i class="far fa-user"></i>Apprentis</a>
                      </li>
                    </ul>
                </nav>
            </div>
        </aside>
        <!-- END MENU SIDEBAR-->
</template>

<style scoped>

</style>