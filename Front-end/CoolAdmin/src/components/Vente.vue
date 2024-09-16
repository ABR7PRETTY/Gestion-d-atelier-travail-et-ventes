<script setup>


</script>

<template>
  <div class="main-content">
    <div class="section__content section__content--p30">
      <div class="container-fluid">
        <div class="row form-group" style="color: #6f42c1; font-size: 1.8em">
          <div class="col col-md-9">
            <div class="form-check-inline form-check" v-for="atelier in ateliers" :key="atelier.id">
              <input type="radio"  :value="atelier" id="inline-radio1" style="width: 30px" name="inline-radios" @change="selectAtelier(atelier)" v-model="currentAtelier" >{{atelier.nom}}
            </div>
          </div>
        </div>


          <div class="form-group">
            <label for="cc-number" class="control-label mb-1">Mois</label>
            <input  type="month" style="height: 50px; width: 300px" class="form-control" aria-required="true" aria-invalid="false" v-model="currentMois" @change="selectMois(currentMois)">
          </div>
        <div class="row">

          <div class="table-responsive table--no-card m-b-30">
            <table class="table table-borderless table-striped table-earning">
              <thead >
              <tr>
                <th>Date</th>
                <th>Quantité</th>
                <th>Article</th>
                <th>Prix</th>
                <th>Action</th>
              </tr>
              </thead>
              <tbody>
              <template v-for="categorie in categories" :key="categorie.id">
                <!-- Ligne de la catégorie -->
                <tr>
                  <td colspan="4" style="text-align: center; background-color: rgba(146,234,169,0.62); font-weight: bold; font-size: 2em; letter-spacing: 20px ; color: #8d02e5; text-transform: uppercase">{{ categorie.libelle }}</td>
                  <td style="background-color: rgba(146,234,169,0.62);" ><i class="fa fa-plus-circle" style="font-size: 1.5em;margin-left: 20px; margin-top: 10px; color: green" @click="this.vente.atelier_id=this.currentAtelier.id;this.vente.mois=this.currentMois;SaveCategorie = categorie;" data-toggle="modal" data-target="#Add"></i></td>
                </tr>
                <tr >
                  <td colspan="5" style="font-size: 0.01em; text-align: center; background-color: rgba(126,180,160,0.68)">-</td>
                </tr>

                <!-- Ventes de la catégorie -->
                <template v-for="item in ventes" >

                    <tr style="font-size: 1.5em" v-if=" item.atelier === currentAtelier.nom &&  item.mois === currentMois && item.categorie===categorie.libelle">
                      <td>{{ item.date }}</td>
                      <td>{{ item.quantite }}</td>
                      <td>{{ item.article}}</td>
                      <td>{{ item.prix }}</td>
                      <td>
                        <i class="fa fa-pencil-alt" style="font-size: 1.1em; color: #c69500; margin-right: 20px" @click="showEditModal(item)" data-toggle="modal" data-target="#Edit"></i>
                        <template v-if="item.id!==choisS">
                          <i class="fa fa-trash-alt" style="font-size: 1.1em; color: #bd2130" @click="choisS=item.id"></i>
                        </template>
                        <template v-if="item.id===choisS">
                          <button class="btn btn-danger" @click="deleteVente(item.id)" style="margin-right: 10px">Sûr?</button>
                          <button class="btn btn-outline-primary" @click="choisS=0">Non</button>
                        </template>
                      </td>
                    </tr>

                </template>
              </template>
              </tbody>

            </table>
          </div>
        </div>
        <div class="row">
          <div class="col-md-12">
            <div class="copyright">
              <marquee style=" margin-top: 2px; width: 450px; font-family: 'Microsoft JhengHei UI'">
                <p style="color: rgba(102,102,102,0.89)"> @ABR7  &emsp; 00228 93 38 25 76</p>
              </marquee>
              <p>Copyright © 2018 Colorlib. All rights reserved. Template by <a href="https://colorlib.com">Colorlib</a>.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>


  <div class="modal fade" id="Add" tabindex="-1" role="dialog" aria-labelledby="mediumModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="mediumModalLabel">Vente</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body" style="margin-left: 100px">
          <div class="col-lg-10">
            <div class="card">
              <div class="card-header" style="color: white; background-color: #6f42c1">Nouvelle vente</div>
              <div class="card-body">
                <div class="card-title">
                  <h3 class="text-center title-2" style="color: #6f42c1">Veuillez remplir les champs</h3>
                </div>
                <hr>
                <form  @submit.prevent="addVente">
                  <div class="form-group">
                    <label  class="control-label mb-1">Date</label>
                    <input  type="number" class="form-control" aria-required="true" aria-invalid="false" v-model="vente.date">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Quantite</label>
                    <div v-if="errorMessage" class="alert alert-danger">
                      {{ errorMessage }}
                    </div>
                    <input  type="number" class="form-control cc-name valid" v-model="vente.quantite">
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Article</label>
                    <select class="form-control" v-model="vente.article">
                      <template v-for="article in articles">
                        <option v-if="article.atelier === currentAtelier.nom && article.categorie===SaveCategorie.libelle" :key="article.id" :value="article">
                          {{ article.libelle }}
                        </option>
                      </template>
                    </select>
                  </div>
                  <div v-if="Message" class="alert alert-success">
                    {{ Message }}
                  </div>
                  <div class="modal-footer" style="margin-right: 130px">
                    <i class="fa fa-reply"  style="font-size: 3em; color: #bd2130; margin-right: 100px" data-dismiss="modal"><h4>Retour </h4></i>
                    <button type="submit" > <i class="fa fa-check"  style="font-size: 3em; color: #00b26f" ><h4>Save </h4> </i> </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="modal fade" id="Edit" tabindex="-1" role="dialog" aria-labelledby="mediumModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="mediumModalLabel">Vente</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body" style="margin-left: 100px">
          <div class="col-lg-10">
            <div class="card">
              <div class="card-header" style="color: white; background-color: #6f42c1">Modification Vente</div>
              <div class="card-body">
                <div class="card-title">
                  <h3 class="text-center title-2" style="color: #6f42c1">Veuillez remplir les champs</h3>
                </div>
                <hr>
                <form  @submit.prevent="editVente(currentVente.id)">
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Atelier</label>
                    <select class="form-control" v-model="currentAtelier">
                      <option v-for="atelier in ateliers" :key="atelier.id" :value="atelier">
                        {{ atelier.nom }}
                      </option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Mois</label>
                    <input  type="month" class="form-control" aria-required="true" aria-invalid="false" v-model="currentVente.mois">
                  </div>
                  <div class="form-group">
                    <label  class="control-label mb-1">Date</label>
                    <input  type="number" class="form-control" aria-required="true" aria-invalid="false" v-model="currentVente.date">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Quantite</label>
                    <input  type="number" class="form-control cc-name valid" v-model="currentVente.quantite">
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Categorie</label>
                    <select class="form-control" v-model="currentCategorie">
                      <option v-for="categorie in categories" :key="categorie.id" :value="categorie">
                        {{ categorie.libelle }}
                      </option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Article</label>
                    <select class="form-control" v-model="currentVente.article">
                      <template v-for="article in articles">
                        <option v-if="article.atelier === currentAtelier.nom && article.categorie===currentCategorie.libelle" :key="article.id" :value="article">
                          {{ article.libelle }}
                        </option>
                      </template>
                    </select>
                  </div>
                  <div v-if="ModifMessage" class="alert alert-success">
                    {{ ModifMessage }}
                  </div>
                  <div v-if="ModiferrorMessage" class="alert alert-danger">
                    {{ ModiferrorMessage }}
                  </div>

                  <div class="modal-footer" style="margin-right: 130px">
                    <i class="fa fa-reply"  style="font-size: 3em; color: #bd2130; margin-right: 100px" data-dismiss="modal"><h4>Cancel </h4></i>
                    <button type="submit"> <i class="fa fa-check"  style="font-size: 3em; color: #00b26f" ><h4>Save </h4> </i> </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  data(){
    return{
      vente:{
        article_id:'',
        artelier_id:'',
        categorie_id:'',
        mois:'',
        prix:'',
        quantite:'',
        date:'',
        article:{},
      },
      currentVente: {},
      currentAtelier: JSON.parse(localStorage.getItem('atelier')),
      currentCategorie: {},
      SaveCategorie: {},
      currentMois: localStorage.getItem('mois'),
      articles:[],
      ateliers:[],
      categories:[],
      ventes:[],
      errorMessage: null,
      Message: null,
      ModiferrorMessage: null,
      ModifMessage: null,
      choisS:0
    };
  },
  mounted() {
    this.listVente();
    this.listAtelier();
    this.listArticle();
    this.listCategorie();
  },
  methods: {
    async listVente(){
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/ventes')
        this.ventes=response.data
      }catch (error){
        console.error(error)
      }
    },

    async listArticle() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/articles');
        this.articles = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async listCategorie() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/categories');
        this.categories = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async listAtelier() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/ateliers');
        this.ateliers = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async addVente() {
      this.vente.atelier_id=this.currentAtelier.id
      this.vente.categorie_id=this.SaveCategorie.id
      this.vente.mois=this.currentMois
      if (this.vente.article.quantite >= this.vente.quantite && this.vente.quantite >0 && this.vente.date > 0 && this.vente.date<31){
        this.vente.prix=this.vente.article.prix*this.vente.quantite
        const formData = new FormData();
        formData.append('date', this.vente.date);
        formData.append('prix', this.vente.prix);
        formData.append('quantite', this.vente.quantite);
        formData.append('article_id', this.vente.article.id);
        formData.append('atelier_id', this.vente.atelier_id);
        formData.append('categorie_id', this.vente.categorie_id);
        formData.append('mois', this.vente.mois);

        try {
          await axios.post('http://127.0.0.1:5000/api/michelin/ventes', formData, {
            headers: { 'Content-Type': 'multipart/form-data' }
          });
          this.errorMessage=null
          this.Message = 'Enregistrement Reussi';
          this.vente = {};
          await this.listVente();
        } catch (error) {
          console.error('Error:', error);
        }
      }else {
        this.Message=null
        this.errorMessage = 'Quantité insuffisant';
      }
    },
    async editVente(id) {
      if(this.currentVente.quantite<=this.currentVente.article.quantite && this.currentVente.quantite >0 && this.currentVente.date > 0 && this.currentVente.date<31){
        this.currentVente.prix=this.currentVente.article.prix*this.currentVente.quantite
        const formData = new FormData();
        formData.append('date', this.currentVente.date);
        formData.append('prix', this.currentVente.prix);
        formData.append('quantite',this.currentVente.quantite);
        formData.append('article_id', this.currentVente.article.id);
        formData.append('atelier_id', this.currentAtelier.id);
        formData.append('categorie_id', this.currentCategorie.id);
        formData.append('mois', this.currentMois)

        try {
          await axios.put(`http://127.0.0.1:5000/api/michelin/updateVente/${id}`, formData, {
            headers: { 'Content-Type': 'multipart/form-data' }
          });
          this.ModifMessage="Modification reussie"
          this.ModiferrorMessage=null
          this.currentVente = {};
          this.currentCategorie = {};
          await this.listVente();
        } catch (error) {
          console.error('Error:', error);
        }
      }else{
        this.ModifMessage=null
        this.ModiferrorMessage="quantité invalide ou insuffisant"
      }

    },
    async deleteVente(id) {
      try {
        await axios.delete(`http://127.0.0.1:5000/api/michelin/deleteVente/${id}`);
        await this.listVente();
      } catch (error) {
        console.error(error);
      }
    },
    showEditModal(vente) {
      this.currentVente = { ...vente };
    },

    selectAtelier(newAtelier) {
      this.currentAtelier = newAtelier;

      // Mettre à jour dans localStorage
      localStorage.setItem('atelier', JSON.stringify(this.currentAtelier));

    },

    selectMois(newMois) {
      this.currentMois = newMois;

      // Mettre à jour dans localStorage
      localStorage.setItem('mois',this.currentMois);

    },

  },


  props:{}
};
</script>

<style scoped>

</style>