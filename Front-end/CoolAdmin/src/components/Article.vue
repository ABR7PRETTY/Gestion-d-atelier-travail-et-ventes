<script setup>


</script>

<template>
  <div class="main-content">
    <div class="section__content section__content--p30">
      <div class="container-fluid">
        <div class="row form-group" style="color: #6f42c1; font-size: 1.8em">
          <div class="col col-md-9">
            <div class="form-check-inline form-check" v-for="atelier in ateliers" :key="atelier.id">
              <input type="radio"  :value="atelier" id="inline-radio1" style="width: 30px" name="inline-radios"  v-model="currentAtelier" @change="selectAtelier(atelier)" >{{atelier.nom}}
            </div>
          </div>
        </div>
        <button type="button" class="btn btn-outline-success btn-lg" style="margin-bottom:70px; font-size: 1.8em" @click="this.article.atelier_id=this.currentAtelier.id; this.article.categorie_id=null;" data-toggle="modal" data-target="#Add"><i class="fa fa-plus-square"></i> Ajouter</button>
        <div class="row">

          <div class="table-responsive table--no-card m-b-30">
            <table class="table table-borderless table-striped table-earning">
              <thead >
              <tr>
                <th>Libellé</th>
                <th>Prix</th>
                <th>Quantité</th>
                <th>Action</th>
              </tr>
              </thead>
              <tbody>
              <template v-for="(categorie) in categories" :key="categorie.id">
                <!-- Ligne de la catégorie -->
                <tr>
                  <td colspan="3" style="text-align: center; background-color: rgba(146,234,169,0.62); font-weight: bold; font-size: 2em; letter-spacing: 20px ; color: #8d02e5; text-transform: uppercase">{{ categorie.libelle }}</td>
                  <td style="background-color: rgba(146,234,169,0.62);" ><i class="fa fa-plus-circle" style="font-size: 1.5em;margin-left: 20px; margin-top: 10px; color: green" @click="this.article.atelier_id=this.currentAtelier.id; this.article.categorie_id = categorie.id;" data-toggle="modal" data-target="#Add"></i></td>
                </tr>
                <tr >
                  <td colspan="5" style="font-size: 0.01em; text-align: center; background-color: rgba(126,180,160,0.68)">-</td>
                </tr>

                <!-- Articles de la catégorie -->
                <template v-for="item in articles">
                  <template v-if="item.atelier===currentAtelier.nom" >
                  <tr style="font-size: 1.5em" v-if="item.categorie === categorie.libelle">

                    <td>{{ item.libelle }}</td>
                    <td>{{ item.prix }}</td>
                    <td>{{ item.quantite }}</td>

                    <td>
                      <i class="fa fa-pencil-alt" style="font-size: 1.1em; color: #c69500; margin-right: 20px" @click="showEditModal(item)" data-toggle="modal" data-target="#Edit"></i>
                      <i class="fa fa-trash-alt" style="font-size: 1.1em; color: #bd2130" @click="deleteArticle(item.id)"></i>
                    </td>
                  </tr>
                  </template>
                </template>
              </template>
              </tbody>

            </table>
          </div>
          </div>
        <div class="row">
          <div class="col-md-12">
            <div class="copyright">
              <marquee style=" margin-top: 2px">
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
          <h5 class="modal-title" id="mediumModalLabel">Article</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body" style="margin-left: 100px">
          <div class="col-lg-10">
            <div class="card">
              <div class="card-header" style="color: white; background-color: #6f42c1">Nouvelle Article</div>
              <div class="card-body">
                <div class="card-title">
                  <h3 class="text-center title-2" style="color: #6f42c1">Veuillez remplir les champs</h3>
                </div>
                <hr>
                <form  @submit.prevent="addArticle">
                  <div class="form-group">
                    <label  class="control-label mb-1">Libelle</label>
                    <input  type="text" class="form-control" aria-required="true" aria-invalid="false" v-model="article.libelle">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Prix</label>
                    <input  type="number" class="form-control cc-name valid" v-model="article.prix">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Quantite</label>
                    <input  type="number" class="form-control cc-name valid" v-model="article.quantite">
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Categorie</label>
                    <select class="form-control" v-model="article.categorie_id">
                      <option v-for="categorie in categories" :key="categorie.id" :value="categorie.id">
                        {{ categorie.libelle }}
                      </option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Atelier</label>
                    <select class="form-control" v-model="article.atelier_id">
                      <option v-for="atelier in ateliers" :key="atelier.id" :value="atelier.id">
                        {{ atelier.nom}}
                      </option>
                    </select>
                  </div>
                  <div v-if="Message" class="alert alert-success">
                    {{ Message }}
                  </div>
                  <div v-if="errorMessage" class="alert alert-danger">
                    {{ errorMessage }}
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
          <h5 class="modal-title" id="mediumModalLabel">Article</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body" style="margin-left: 100px">
          <div class="col-lg-10">
            <div class="card">
              <div class="card-header" style="color: white; background-color: #6f42c1">Modification Article</div>
              <div class="card-body">
                <div class="card-title">
                  <h3 class="text-center title-2" style="color: #6f42c1">Veuillez remplir les champs</h3>
                </div>
                <hr>
                <form  @submit.prevent="editArticle(currentArticle.id)">
                  <div class="form-group">
                    <label  class="control-label mb-1">Libelle</label>
                    <input  type="text" class="form-control" aria-required="true" aria-invalid="false" v-model="currentArticle.libelle">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Prix</label>
                    <input  type="text" class="form-control cc-name valid" v-model="currentArticle.prix">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Quantite</label>
                    <input  type="text" class="form-control cc-name valid" v-model="currentArticle.quantite">
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Categorie</label>
                    <select class="form-control" v-model="currentArticle.categorie_id">
                      <option v-for="categorie in categories" :key="categorie.id" :value="categorie.id">
                        {{ categorie.libelle }}
                      </option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Atelier</label>
                    <select class="form-control" v-model="currentArticle.atelier_id">
                      <option v-for="atelier in ateliers" :key="atelier.id" :value="atelier.id">
                        {{ atelier.nom }}
                      </option>
                    </select>
                  </div>
                  <div v-if="Message" class="alert alert-success">
                    {{ Message }}
                  </div>
                  <div v-if="errorMessage" class="alert alert-danger">
                    {{ errorMessage }}
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
      article:{
        libelle:'',
        prix:'',
        quantite:'',
        categorie_id:'',
        atelier_id:'',
      },
      currentArticle: {},
      currentAtelier: JSON.parse(localStorage.getItem('atelier')),
      categories:[],
      ateliers:[],
      articles:[],
      Message:null,
      errorMessage:null,
      ModiferrorMessage:null,
      ModifMessage:null
    };
  },
  mounted() {
    this.listArticle();
    this.listAtelier();
    this.listCategorie()
  },
  methods: {
    async listArticle(){
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/articles')
        this.articles=response.data

      }catch (error){
        console.error(error)
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
    async addArticle() {
      if(this.article.prix >0 && this.article.quantite>0){
        const formData = new FormData();
        formData.append('libelle', this.article.libelle);
        formData.append('prix', this.article.prix);
        formData.append('quantite', this.article.quantite);
        formData.append('categorie_id', this.article.categorie_id);
        formData.append('atelier_id', this.article.atelier_id);

        try {
          await axios.post('http://127.0.0.1:5000/api/michelin/articles', formData, {
            headers: { 'Content-Type': 'multipart/form-data' }
          });
          this.Message="Enregistrement reussi"
          this.errorMessage=null
          this.article = {};
          await this.listArticle();
        } catch (error) {
          console.error('Error:', error);
        }
      }else {
        this.Message=null
        this.errorMessage="Quantité ou prix invalide"
      }

    },
    async editArticle(id) {
      if(this.currentArticle.prix >0 && this.currentArticle.quantite>0){
        const formData = new FormData();
        formData.append('libelle', this.currentArticle.libelle);
        formData.append('prix', this.currentArticle.prix);
        formData.append('quantite',this.currentArticle.quantite)
        formData.append('categorie_id', this.currentArticle.categorie_id)
        formData.append('atelier_id', this.currentArticle.atelier_id)

        try {
          await axios.put(`http://127.0.0.1:5000/api/michelin/updateArticle/${id}`, formData, {
            headers: { 'Content-Type': 'multipart/form-data' }
          });
          this.ModifMessage="Modification reussie"
          this.ModiferrorMessage=null
          this.currentArticle = {};
          await this.listArticle();
          localStorage.setItem('atelier', JSON.stringify(this.currentAtelier));
          console.log(this.currentAtelier)
        } catch (error) {
          console.error('Error:', error);
        }
      }else{
        this.ModiferrorMessage="Prix ou quantite invalide"
        this.ModifMessage=null
      }

    },
    async deleteArticle(id) {
      try {
        await axios.delete(`http://127.0.0.1:5000/api/michelin/deleteArticle/${id}`);
        await this.listArticle();
      } catch (error) {
        console.error(error);
      }
    },
    showEditModal(article) {
      this.currentArticle = { ...article };
    },
    selectAtelier(newAtelier) {
      this.currentAtelier = newAtelier;

      // Mettre à jour dans localStorage
      localStorage.setItem('atelier', JSON.stringify(this.currentAtelier));

    },

  },


  props:{}
};
</script>

<style scoped>

</style>