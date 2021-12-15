<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>COURSES</h1>
        <hr><br><br>
        <alert v-if="showMessage" :message="message" />
        <button v-b-modal.book-modal type="button" class="btn btn-success btn-sm">Add</button>
        &nbsp;
        <button v-b-modal.search-modal type="button" class="btn btn-success btn-sm">Search</button>
        &nbsp;
        <button type="button" class="btn btn-success btn-sm" @click="getBooks()">Flush</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Course_ID</th>
              <th scope="col">Course_NAME</th>
              <th scope="col">DEPT_NAME</th>
              <th scope="col">Course_Eng_NAME</th>
              <th scope="col">CREDIT</th>
              <th />
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.course_id }}</td>
              <td>{{ book.course_name }}</td>
              <td>{{ book.dept_id }}</td>
              <td>{{ book.course_eng_name }}</td>
              <td>{{ book.credit }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                    v-b-modal.book-update-modal
                    type="button"
                    class="btn btn-warning btn-sm"
                    @click="editBook(book)"
                  >
                    Update
                  </button>
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="onDeleteBook(book)"
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal
      id="book-modal"
      ref="addBookModal"
      title="Add a new course"
      hide-footer
    >
      <b-form class="w-100" @submit="onSubmit" @reset="onReset">
        <b-form-group
          id="form-title-group"
          label="Course_ID:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            v-model="addBookForm.course_id"
            type="text"
            required
            placeholder="Enter Course_ID"
          />
        </b-form-group>
        <b-form-group
          id="form-author-group"
          label="Course_NAME:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            v-model="addBookForm.course_name"
            type="text"
            required
            placeholder="Enter Course_name"
          />
        </b-form-group>
        <b-form-group
          id="form-dept-group"
          label="DEPT_ID:"
          label-for="form-dept-input"
        >
          <b-form-input
            id="form-dept-input"
            v-model="addBookForm.dept_id"
            type="text"
            required
            placeholder="Enter dept_id"
          />
        </b-form-group>
        <b-form-group
          id="form-coeng-group"
          label="Course_Eng_NAME:"
          label-for="form-coeng-input"
        >
          <b-form-input
            id="form-coeng-input"
            v-model="addBookForm.course_eng_name"
            type="text"
            required
            placeholder="Enter Course_Eng_NAME"
          />
        </b-form-group>
        <b-form-group
          id="form-cedit-group"
          label="Course_Credit:"
          label-for="form-credit-input"
        >
          <b-form-input
            id="form-credit-input"
            v-model="addBookForm.credit"
            type="text"
            required
            placeholder="Enter Course_Credit"
          />
        </b-form-group>
        <!-- <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addBookForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group> -->
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal
      id="book-update-modal"
      ref="editBookModal"
      title="Update"
      hide-footer
    >
      <b-form class="w-100" @submit="onSubmitUpdate" @reset="onResetUpdate">
        <b-form-group
          id="form-title-group"
          label="Course_ID:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            v-model="editForm.course_id"
            type="text"
            required
            placeholder="Enter Course_ID"
          />
        </b-form-group>
        <b-form-group
          id="form-author-group"
          label="Course_NAME:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            v-model="editForm.course_name"
            type="text"
            required
            placeholder="Enter Course_name"
          />
        </b-form-group>
        <b-form-group
          id="form-dept-group"
          label="DEPT_ID:"
          label-for="form-dept-input"
        >
          <b-form-input
            id="form-dept-input"
            v-model="editForm.dept_id"
            type="text"
            required
            placeholder="Enter dept_id"
          />
        </b-form-group>
        <b-form-group
          id="form-coeng-group"
          label="Course_Eng_NAME:"
          label-for="form-coeng-input"
        >
          <b-form-input
            id="form-coeng-input"
            v-model="editForm.course_eng_name"
            type="text"
            required
            placeholder="Enter Course_Eng_NAME"
          />
        </b-form-group>
        <b-form-group
          id="form-cedit-group"
          label="Course_Credit:"
          label-for="form-credit-input"
        >
          <b-form-input
            id="form-credit-input"
            v-model="editForm.credit"
            type="text"
            required
            placeholder="Enter Course_Credit"
          />
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>

    <b-modal
      id="search-modal"
      ref="searchBookModal"
      title="Search"
      hide-footer
    >
      <b-form class="w-100" @submit="onSearch" @reset="onReset">
        <b-form-group
          id="form-title-group"
          label="Course_ID:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            v-model="searchForm.course_id"
            type="text"
            required
            placeholder="Enter Course_ID"
          />
        </b-form-group>
        <b-form-group
          id="form-author-group"
          label="Course_NAME:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            v-model="searchForm.course_name"
            type="text"
            required
            placeholder="Enter Course_name"
          />
        </b-form-group>
        <b-form-group
          id="form-dept-group"
          label="DEPT_ID:"
          label-for="form-dept-input"
        >
          <b-form-input
            id="form-dept-input"
            v-model="searchForm.dept_id"
            type="text"
            required
            placeholder="Enter dept_id"
          />
        </b-form-group>
        <b-form-group
          id="form-coeng-group"
          label="Course_Eng_NAME:"
          label-for="form-coeng-input"
        >
          <b-form-input
            id="form-coeng-input"
            v-model="searchForm.course_eng_name"
            type="text"
            required
            placeholder="Enter Course_Eng_NAME"
          />
        </b-form-group>
        <b-form-group
          id="form-cedit-group"
          label="Course_Credit:"
          label-for="form-credit-input"
        >
          <b-form-input
            id="form-credit-input"
            v-model="searchForm.credit"
            type="text"
            required
            placeholder="Enter Course_Credit"
          />
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'
import Alert from '@/components/Alert.vue'

export default {
  components: {
    alert: Alert
  },
  data() {
    return {
      books: [],
      addBookForm: {
        course_id: '',
        course_name: '',
        dept_id: '',
        course_eng_name: '',
        credit: ''
      },
      message: '',
      showMessage: false,
      editForm: {
        course_id: '',
        course_name: '',
        dept_id: '',
        course_eng_name: '',
        credit: ''
      },
      searchForm: {
        course_id: '',
        course_name: '',
        dept_id: '',
        course_eng_name: '',
        credit: ''
      },
    }
  },
  created() {
    this.getBooks()
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/books'
      axios.get(path)
        .then((res) => {
          this.books = res.data.books
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        })
    },
    addBook(payload) {
      const path = 'http://localhost:5000/books'
      axios.post(path, payload)
        .then(() => {
          this.getBooks()
          this.message = 'Course added!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks()
        })
    },
    searchBook(payload) {
        const path = 'http://localhost:5000/courses/search'
        axios.post(path, payload)
            .then((res) => {
                this.books = res.data.books
            })
            .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            })
    },
    initForm() {
      this.addBookForm.course_id = ''
      this.addBookForm.course_name = ''
      this.addBookForm.dept_id = ''
      this.addBookForm.course_eng_name = ''
      this.addBookForm.credit = ''

      this.editForm.course_id = ''
      this.editForm.course_name = ''
      this.editForm.dept_id = ''
      this.editForm.course_eng_name = ''
      this.editForm.credit = ''

      this.searchForm.course_id = ''
      this.searchForm.course_name = ''
      this.searchForm.dept_id = ''
      this.searchForm.course_eng_name = ''
      this.searchForm.credit = ''
    },
    onSubmit(evt) {
      evt.preventDefault()
      this.$refs.addBookModal.hide()
      // let read = false;
      // if (this.addBookForm.read[0]) read = true;
      const payload = {
        course_id: this.addBookForm.course_id,
        course_name: this.addBookForm.course_name,
        dept_id: this.addBookForm.dept_id,
        course_eng_name: this.addBookForm.course_eng_name,
        credit: this.addBookForm.credit
      }
      this.addBook(payload)
      this.initForm()
    },
    onSearch(evt) {
      evt.preventDefault()
      this.$refs.searchBookModal.hide()
      // let read = false;
      // if (this.addBookForm.read[0]) read = true;
      const payload = {
        course_id: this.searchForm.course_id,
        course_name: this.searchForm.course_name,
        dept_id: this.searchForm.dept_id,
        course_eng_name: this.searchForm.course_eng_name,
        credit: this.searchForm.credit
      }
      this.searchBook(payload)
      this.initForm()
    },
    onReset(evt) {
      evt.preventDefault()
      this.$refs.addBookModal.hide()
      this.initForm()
    },
    editBook(book) {
      this.editForm = book
    },
    onSubmitUpdate(evt) {
      evt.preventDefault()
      this.$refs.editBookModal.hide()
      // let read = false;
      // if (this.editForm.read[0]) read = true;
      const payload = {
        course_id: this.editForm.course_id,
        course_name: this.editForm.course_name,
        dept_id: this.editForm.dept_id,
        course_eng_name: this.editForm.course_eng_name,
        credit: this.editForm.credit
      }
      this.updateBook(payload, this.editForm.course_id)
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:5000/books/${bookID}`
      axios.put(path, payload)
        .then(() => {
          this.getBooks()
          this.message = 'Course updated!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks()
        })
    },
    onResetUpdate(evt) {
      evt.preventDefault()
      this.$refs.editBookModal.hide()
      this.initForm()
      this.getBooks() // why?
    },
    removeBook(bookID) {
      const path = `http://localhost:5000/books/${bookID}`
      axios.delete(path)
        .then(() => {
          this.getBooks()
          this.message = 'Course removed!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks()
        })
    },
    onDeleteBook(book) {
      this.removeBook(book.course_id)
    }
  }
}
</script>
